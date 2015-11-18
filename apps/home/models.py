#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class QRCode(models.Model):
    '''扫码登录'''
    qrcode_id = models.CharField(u'二维码id', max_length=50)
    type = models.IntegerField(u'二维码类型')
    dip = models.CharField(u'产品代码', max_length=20)
    diu = models.CharField(u'设备唯一标示', max_length=100)
    created_time = models.DateTimeField(u"创建时间", auto_now_add=True)
    last_update = models.DateTimeField(u'最近更新时间', auto_now=True)

    class Meta:
        db_table = 'qrcode_qrcode'