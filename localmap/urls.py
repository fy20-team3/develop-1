from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewspot, name='viewspot'),
    path('hotelspot', views.hotelspot,name='hotelspot')
]
