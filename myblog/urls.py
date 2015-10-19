"""myblog URL Configuration

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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', "apps.home.view.homepage"),
    url(r'^redis_cache/', "apps.home.view.redis_cache"),
    url(r'^memcached_cache/', "apps.home.view.memcached_cache"),
    url(r'^ocs_cache/', "apps.home.view.ocs_cache"),
    url(r'^kvs_cache/', "apps.home.view.kvs_cache"),
    url(r'^send_mail/', "apps.home.view.send_mail"),
]
