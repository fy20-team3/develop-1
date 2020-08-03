from django.urls import path
from . import views

urlpatterns = [
    path('', views.entrance, name='entrance'),
    path('viewspot', views.viewspot, name='viewspot'),
    path('hotelspot', views.hotelspot,name='hotelspot'),
    path('tripplan', views.tripplan,name='tripplan')
]
