from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ocr/', views.les_factures, name='factures'),
    path('ocr/details/<str:pk>/', views.traitement, name='ocr'),
    path('export/<str:pk>/', views.export_to_excel, name='export_to_excel'),
]
