from django.urls import path

from . import views

urlpatterns = [
    path('companion', views.companionpage, name='companionpage'),
    path('submit', views.submitpage, name='submitpage'),
    path('<str:userid>/submitdata/', views.submitdata, name='submitdata'),
    path('logs', views.logpage, name='logpage'),
]