from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_item/', views.show_item, name='show_item')
]