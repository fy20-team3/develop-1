from django.urls import path
from . import views

#namespaceの設定
app_name = 'mymap'

urlpatterns = [
 path('', views.index, name='index'),
 path('signup/', views.SignUp.as_view(), name='signup'), 
 path('login/', views.Login.as_view(), name='login')

]
