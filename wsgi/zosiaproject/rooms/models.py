from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from common.helpers import *

# feature tasks (microbacklog ;) )
# - blocking datatimes
# - unblocking at specified time
# - actually _working_ locators fields
# - set pass / leave room 
# - js dialog boxes
# - merging
# - deploy
# - password should not be a pass but token (or maybe default pass should be autogenerated)

# most of non-standard fuss here is about serializing
# and caching rooms in database;
# this probably should be moved into different module
# for usage with built-in django serialization framework
#
# note: caching does not work with lock times atm
# repair this if required after stresstests

class RoomManager(models.Manager):
    # this class does basic caching for json data
    # when any of room changes then flag update_required
    # should be set to True
    # this flag prevents database lookup for creating json data

    cache = ""
    update_required = True
    
    def to_json(self, request=None):
        if self.update_required:
            self.cache = [ x.to_json(request) for x in self.filter(hidden=False) ]
            # self.update_required = False # comment this line to disable caching
        return '[{}]'.format(','.join(self.cache))


class Room(models.Model):
    number              = models.CharField(max_length=16)
    capacity            = models.PositiveIntegerField()
    description         = models.CharField(max_length=255, null=True, blank=True)
    password            = models.CharField(max_length=16)

    hidden = models.BooleanField(default=False)

    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='UserInRoom')

    # unlock time for first locator
    short_unlock_time   = models.DateTimeField()
    #long unlock time
    #long_unlock_time   = models.DateTimeField()

    # ok, this probably shouldn't be done this way, but proper one-to-many
    # relation requires changing user model which can't be done now
    # this should be refactored after ZOSIA09
    # locators = models.ManyToManyField(User, through='RoomMembership')
    objects = RoomManager()

    class Meta:
        ordering = ('number',)

    def get_no_locators(self):
        return UserInRoom.objects.filter(room=self.id).count()

    def get_status(self, request=None):
        if is_rooming_disabled(request): return 3 # zapisy są zamknięte
        no_locators = self.get_no_locators()

        # doesnt' matter what, if room is empty, it is unlocked
        if not no_locators:
            return 0 
        if no_locators >= self.capacity:
            return 2 # room is full

        # short unlock time is still in future
        if self.short_locked():
            return 1
        #if self.password != "":
        #    return 1 # password is set
        
        return 0     # default; it's ok to sign into room


    def to_json(self, request=None):
        # json format:
        # id - number
        # st - status
        # nl - number of locators
        # mx - max room capacity
        # lt - unlock time (optional)
        # features? (optional)
        #"""[{"id":"id","st":0,"nl":0,"mx":1}]"""


        no_locators = self.get_no_locators()
        status= self.get_status(request)
        # this is soo wrong... (but works)
        optional = ''
        # short unlock time is in the future
        if self.short_locked():
            optional = ',"lt":"%s"' % ( self.short_unlock_time.ctime()[10:-8] )

        return '{"id":"%s","st":%s,"nl":%s,"mx":%s%s, "dsc":"%s"}' % (self.number,
                status, no_locators, self.capacity, optional, self.description)


    def short_locked(self):
        # returns true when time is still in future
        ret = self.short_unlock_time > timezone.now()
        return ret


    #def save(self):
    #    super(NRoom, self).save()
    #    # set cached data in manager to be updated
    #    # self.__class__.objects.update_required = True

    def __str__(self):
        return str(self.number)


class UserInRoom(models.Model):
    # user-room-ownership relation #FIXME: it REALLY should be better implemented...
    locator   = models.OneToOneField(settings.AUTH_USER_MODEL)
    room      = models.ForeignKey(Room)
    ownership = models.BooleanField()

    def firstname(self):
        return self.locator.first_name

    def lastname(self):
        return self.locator.last_name

    class Meta:
        ordering = ['locator__last_name', 'locator__first_name']
