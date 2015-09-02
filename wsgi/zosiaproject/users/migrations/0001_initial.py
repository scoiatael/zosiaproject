# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('email', models.EmailField(verbose_name='adres email', max_length=254, unique=True)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('is_active', models.BooleanField(help_text='Oznacza czy użytkownika należy uważać za aktywnego. Odznacz to, zamiast usuwać konta.', verbose_name='aktywny', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='data przyłączenia', default=django.utils.timezone.now)),
                ('committee', models.BooleanField(verbose_name='programme committee', default=False)),
                ('groups', models.ManyToManyField(verbose_name='groups', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, to='auth.Group', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_query_name='user', help_text='Specific permissions for this user.', blank=True, to='auth.Permission', related_name='user_set')),
            ],
            options={
                'verbose_name': 'użytkownik',
                'verbose_name_plural': 'użytkownicy',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=64, default='')),
                ('accepted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Organizacja',
                'verbose_name_plural': 'Organizacje',
            },
        ),
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('day_1', models.BooleanField()),
                ('day_2', models.BooleanField()),
                ('day_3', models.BooleanField()),
                ('breakfast_2', models.BooleanField()),
                ('breakfast_3', models.BooleanField()),
                ('breakfast_4', models.BooleanField()),
                ('dinner_1', models.BooleanField()),
                ('dinner_2', models.BooleanField()),
                ('dinner_3', models.BooleanField()),
                ('bus', models.BooleanField(default=False)),
                ('vegetarian', models.BooleanField()),
                ('paid', models.BooleanField(default=False)),
                ('shirt_size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], max_length=5)),
                ('shirt_type', models.CharField(choices=[('m', 'klasyczna'), ('f', 'żeńska')], max_length=1)),
                ('want_bus', models.BooleanField(default=False)),
                ('minutes_early', models.IntegerField(default=0)),
                ('bus_hour', models.CharField(choices=[('', 'obojętne'), ('16:00', '16:00'), ('18:00', '18:00')], blank=True, max_length=10, default='', null=True)),
                ('photo_url', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(verbose_name='description', max_length=2048, blank=True)),
                ('org', models.ForeignKey(to='users.Organization')),
                ('state', models.ForeignKey(to='common.ZosiaDefinition')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Preferencje',
            },
        ),
        migrations.CreateModel(
            name='Waiting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('day_1', models.BooleanField()),
                ('day_2', models.BooleanField()),
                ('day_3', models.BooleanField()),
                ('state', models.ForeignKey(to='common.ZosiaDefinition')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
