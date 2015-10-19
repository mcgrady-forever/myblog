#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from django.core.cache.backends.memcached import MemcachedCache
from django_bmemcached.memcached import BMemcached

class NoCloseMemcachedBackend(BMemcached):
    '''request结束后不close memcached连接，达到连接持久化效果

    Django的MemcachedCache默认每个request建立memcached连接，request结束close连接，如果连接memcached速度过慢，
    在高并发场景下会导致大量连接memcached的tcp TIME_WAIT状态，详见bug https://code.djangoproject.com/ticket/11331

    此backend重写close方法，request结束时不close连接。参考文章:
    http://blog.memcachier.com/2014/12/12/django-persistent-memcached-connections/
    '''

    def close(self, **kwargs):
        '''request 结束时不close 连接'''
        pass
