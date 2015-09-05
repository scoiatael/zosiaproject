from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list.json$', views.json_rooms_list),
    url(r'^modify/$', views.modify_room),
    url(r'^open/$', views.open_room),
    url(r'^close/$', views.close_room),
    url(r'^trytogetin/$', views.trytogetin_room),
    url(r'^leave/$', views.leave_room),
]
