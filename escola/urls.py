from django.urls import path   # type: ignore
from  . import views
urlpatterns = [
    path('ver_escola', views.ver_escola, name="ver_escola"),
    
    
]