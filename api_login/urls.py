from django.urls import path
from . import views

urlpatterns = [
        path('', views.getForm),
        path('postLoginData', views.postLoginData),
        path('checkLoginData', views.checkLoginData),
        ];
