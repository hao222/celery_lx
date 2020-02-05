from course import views
from django.urls import re_path

urlpatterns = [
    re_path(r'do/$', views.do, name='do')
]