from django.urls import path
from .import views


urlpatterns = [
    path('',views.gallery, name ='gallery'),
    path('pic/<str:pk>/',views.views.viewpic, name ='pic'),
    path('add/',views.addpic, name ='add'),
]
