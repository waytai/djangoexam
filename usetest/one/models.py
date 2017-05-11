# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class IpUser(models.Model):
    name = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.name


class IpRole(models.Model):
    """
    用户角色，例如一级代理商之类
    """
    rolename = models.CharField(max_length=40)
    user = models.ManyToManyField(IpUser, blank=True)

    def __str__(self):
        return self.rolename


class IpPermission(models.Model):
    """
    对应前端勾选的权限
    与IpRole是对多的关系
    """
    permname = models.CharField(max_length=40)
    roleperm = models.ManyToManyField(IpRole)

    def __str__(self):
        return self.pername


class Device(models.Model):
    name = models.CharField(max_length=40, unique=True)
    def __str__(self):
        return self.name


class DeviceOne(models.Model):
    title = models.CharField(max_length=40, unique=True)
    device = models.OneToOneField(Device, blank=True, null=True, help_text='help test')
    def __str__(self):
        return self.title


class DeviceGroup(models.Model):
    """
    设备组
    """
    groupname = models.CharField(max_length=40, unique=True)
    device = models.ManyToManyField(Device)
    user = models.ManyToManyField(IpUser)

    def __str__(self):
        return self.groupname
