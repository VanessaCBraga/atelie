from django.urls import path
from . import views

urlpatterns = [
    path('registrar_reparo/', views.registrar_reparo),
]