from django.conf.urls import url
from django.urls import path
from djtest import views

urlpatterns = [
    path('index/', views.index),
    path('logs/', views.myLogs),
    path('new/', views.new_page),
    url(r'^log/(?P<log_id>[0-9]+)/$', views.log_page, name='log_page'),
    url(r'^log/edit/$', views.modify_flag, name='flag_item'),
    url(r'^log/add/$', views.add_flag, name='flag_add'),
    url('log/end/', views.end_log, name='log_end'),
    url('log/new/', views.new_log, name='log_add'),
]