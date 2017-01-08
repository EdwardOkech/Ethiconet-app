from django.conf.urls import url 
from django.contrib.flatpages import views
from . import views

urlpatterns = [
      url(r'^$', views.homepage, name='homepage'),
      
]