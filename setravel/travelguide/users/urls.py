from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('upinfo/', views.upinfo, name='upinfo'),
    path('uppass/', views.uppass, name='uppass'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),
]
