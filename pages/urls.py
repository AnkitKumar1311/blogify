from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.indexPage, name='home'),

    # path starting with regular expression at the bottom to match at the end
    re_path(r'^@(?P<username>[a-zA-Z0-9\.\-\_\@]+)/$', views.viewUser, name='view_user'),
]