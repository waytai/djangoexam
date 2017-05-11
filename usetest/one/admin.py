from django.contrib import admin
from .models import IpUser, IpRole
from .models import IpPermission
from .models import  DeviceOne, Device


class IpUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password', 'parent')
    search_fields = ('id',)

class IpPermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'permname')
    search_fields = ('id',)

class DeviceOneAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'device')
    search_fields = ('id',)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id',)

admin.site.register(IpUser, IpUserAdmin)
admin.site.register(IpPermission, IpPermissionAdmin)
admin.site.register(DeviceOne, DeviceOneAdmin)
admin.site.register(Device, DeviceAdmin)
