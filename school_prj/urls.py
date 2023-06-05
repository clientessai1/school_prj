"""school_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
admin.autodiscover()
admin.site.site_header = "SySchool ESGIS Admin"
admin.site.site_title = "SySchool ESGIS Admin Portal"
admin.site.index_title = "Welcome to SySchool Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('school_app.urls')), #School_app urls
    path('api1/', include('api1.urls')), #api1_app urls
    path('api_login/', include('api_login.urls')), #api1_app urls
    #path('api_logged_user_pages/', include('api_logged_user_pages.urls')),
    re_path(r'^api_logged_user_pages/', include('api_logged_user_pages.urls')),
    path('create_group_and_users/', include('api_create_group_and_users.urls')), #api1_app urls
]
