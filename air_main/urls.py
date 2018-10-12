from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tested', views.main_view, name='main_view'),
    url(r'^index', views.test_table, name='test_table'),
]