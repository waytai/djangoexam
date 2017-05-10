from django.contrib import admin
from main.models import IpUser, IpRole
from main.models import IpPermission


class IpUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password', 'parent')
    search_fields = ('id', 'company')

class IpPermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'permname', 'roleperm')
    search_fields = ('id', 'company')

admin.site.register(IpUser, IpUserAdmin)
admin.site.register(IpPermission, IpPermissionAdmin)
