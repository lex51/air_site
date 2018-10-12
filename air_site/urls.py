"""air_site URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from air_main.air_main import models
from api.resources import PlainsResource

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('air_main.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^api/', include(PlainsResource().urls)),
]


