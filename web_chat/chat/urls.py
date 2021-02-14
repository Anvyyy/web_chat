from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('reg/', views.registration, name='reg'),
    path('auth/', views.MyLoginView.as_view(), name='auth'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('start/', views.start_chat, name='chat'),
    path('<str:room_name>/', views.chat, name='room'),

]
