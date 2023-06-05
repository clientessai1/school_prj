from django.urls import path, re_path
from . import views

urlpatterns = [
        #path('<user>&<prenoms>', views.getIndex),
        path('', views.getIndex),
        path('page1', views.getPage1),
        path('page2', views.getPage2),
];
