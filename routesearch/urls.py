from django.urls import path
from . import views

app_name = 'routesearch'
urlpatterns = [
 path('', views.index, name='index'),
]
