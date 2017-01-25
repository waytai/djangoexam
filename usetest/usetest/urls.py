"""usetest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from one.views import CreateUse, create_role, assign_use_role, add_permmissions, assign_role_pm
from one.views import create_device, create_device_group, assign_device_to_dgroup
from one.views import assign_dgroup_to_use


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(regex=r'^createuse/', view=CreateUse),
    url(regex=r'^createrole/', view=create_role),
    url(regex=r'^assign_use_role/', view=assign_use_role),
    url(regex=r'^add_permmissions/', view=add_permmissions),
    url(regex=r'^assign_role_pm/', view=assign_role_pm),
    url(regex=r'^create_device/', view=create_device),
    url(regex=r'^create_device_group/', view=create_device_group),
    url(regex=r'^assign_device_to_dgroup/', view=assign_device_to_dgroup),
    url(regex=r'^assign_dgroup_to_use/', view=assign_dgroup_to_use),
]



