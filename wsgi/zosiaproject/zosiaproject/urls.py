"""zosiaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

import blog.views
from blog.feeds import *
import lectures.views
import common.views
#import rooms.views
import users.views

feeds = {
    'blog': LatestBlogEntries,
}

urlpatterns = [
    url(r'^$', blog.views.index),
    url(r'^blog/', include('blog.urls')),
    url(r'^rooms/', include('rooms.urls')),

    # rss feed
    url(r'^feeds/$', LatestBlogEntries()),

    # admin related
    url(r'^admin/register_payment/$', users.views.register_payment),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^committee/', include('committee.urls', namespace='committee')),

    # registration related
    url(r'^register/$', users.views.register),
    url(r'^waiting/$', users.views.waiting_list),
    url(r'^register/thanks/$', users.views.thanks),
    url(r'^register/regulations/$', users.views.regulations),

    url(r'^register/activate/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', users.views.activate_user),

    url(r'^change_preferences/$', users.views.change_preferences),

    # login / logout
    url(r'^login/$', common.views.login_view),
    url(r'^accounts/login/', common.views.login_view),
    url(r'^logout/$', common.views.logout_view),
    url(r'^logout/bye/$', common.views.thanks),

    # apps main urls
    url(r'^lectures/$', lectures.views.index),
    url(r'^program/$', lectures.views.program),

    # urls required for password change/reset
    url(r'^password_change/$', common.views.password_change),
    url(r'^password_change/done/$', common.views.password_change_done),

    url(r'^password_reset/$',
        'django.contrib.auth.views.password_reset',
        { 'template_name':'password_reset_form.html' }, name='password_reset'),
    url(r'^password_reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        { 'template_name':'password_reset_done.html' }, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        { 'template_name':'password_reset_confirm.html' }, name='password_reset_confirm'),
    url(r'^reset/done/$',
        'django.contrib.auth.views.password_reset_complete',
        { 'template_name':'password_reset_complete.html' }, name='password_reset_complete'),
]
