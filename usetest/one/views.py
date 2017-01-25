# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from models import  IpUser, IpRole, IpPermission, Device, DeviceGroup
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from django.http import HttpResponse
import json
from rest_framework.views import APIView
import random

def CreateUse(request):
    """
    创建用户
    """

    ip_use = IpUser.objects.create(name='liu', password='123456')
    ip_use_ch1 = IpUser.objects.create(name='liu1', password='123456', parent=ip_use)
    ip_use_ch2 = IpUser.objects.create(name='liu2', password='123456', parent=ip_use)
    to_json = {'ret':'ok'}
    return HttpResponse(json.dumps(to_json), content_type="application/json")


def Listuse(request):
    """
    列出用户
    """

    admin_use_id = IpUser.objects.get(name='liu').id
    childs = IpUser.objects.filter(parent=admin_use_id)
    to_json = {'ret':'ok'}
    return HttpResponse(json.dumps(to_json), content_type="application/json")


def create_role(request):
    """
    创建角色
    """

    ip_role =  IpRole.objects.create(rolename= u'一级代理商' )
    to_json = {'ret':'ok'}
    return HttpResponse(json.dumps(to_json), content_type="application/json")

def assign_use_role(request):
    """
    指定用户的角色
    """

    ip_uses = IpUser.objects.filter(name='liu1')
    ip_role =  IpRole.objects.get(rolename= u'一级代理商')
    print "-"*20,len(ip_uses)
    print ip_uses, type(ip_uses)
    ip_role.user.add(ip_uses[0], ip_uses[1]) 
    to_json = {'ret':'ok'}
    return HttpResponse(json.dumps(to_json), content_type="application/json")



def add_permmissions(request):
    """
    添加所有的权限
    """
    pms = (u'设备急修',u'设备档案',u'数据统计',u'消息通知',u'账户信息',u'系统设置',
       u'设备监控',u'监控中心',u'单机监控',u'GIS监控 ',u'群组监控',u'设备维修',
       u'维修工单',u'维修记录',u'设备档案',u'设备信息',u'维保记录',u'故障统计',u'运行统计')

    for pm in pms:
        ip_pm = IpPermission()
        ip_pm.permname  = pm
        ip_pm.save()

    to_json = {'ret':'ok'}
    return HttpResponse(json.dumps(to_json), content_type="application/json")


def assign_role_pm(request):
    """
    给角色权限
    """
    ip_role =  IpRole.objects.get(rolename= u'一级代理商')
    ip_device_monitor = IpPermission.objects.get(permname=u'设备监控') 
    ip_device_repair = IpPermission.objects.get(permname=u'维修工单')
    ip_role.ippermission_set.add(ip_device_monitor, ip_device_repair)
    to_json = {'ret':'ok'}
    return HttpResponse(json.dumps(to_json), content_type="application/json")


def create_device(request):
    """
    创建设备
    """
    device_name = 'device'+str(random.randint(0,100))
    device = Device.objects.create(name=device_name)
    to_json = {'ret':'ok'}
    return HttpResponse(json.dumps(to_json), content_type="application/json")


def create_device_group(request):
    """
    创建设备组
    """
    device_group = DeviceGroup()
    device_group.groupname = 'groupone'
    device_group.save()
    to_json = {'ret':'ok'}
    return HttpResponse(json.dumps(to_json), content_type="application/json")


def assign_device_to_dgroup(request):
    """
    分配设备给device_group
    """
    device = Device.objects.get(name='deviceone')
    device_group = DeviceGroup.objects.get(groupname='groupone')
    device_group.device.add(device)
    to_json = {'ret':'ok'}
    return HttpResponse(json.dumps(to_json), content_type="application/json")


def assign_dgroup_to_use(request):
    """
    分配device_group给用户
    """
    device_group = DeviceGroup.objects.get(groupname='groupone')
    ip_use= IpUser.objects.get(pk=2)
    device_group.user.add(ip_use)
    to_json = {'ret':'ok'}
    return HttpResponse(json.dumps(to_json), content_type="application/json")


