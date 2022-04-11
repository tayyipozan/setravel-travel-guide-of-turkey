from django.urls import path
from . import views

urlpatterns = [
    path('', views.placelist, name='placelist'),
    path('adding_place/', views.adding_place, name='adding_place'),
    path('<str:place_title>/', views.detailplace, name='detailplace'),
    path('category/<str:categoryname>/', views.category, name='category'),
    #path('editplace/', views.editplace, name='editplace'),
    #path('removeplace/', views.removeplace, name='removeplace'),
]
