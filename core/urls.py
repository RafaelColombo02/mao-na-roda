
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login', permanent=False)),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('servicos/', views.servicos_view, name='servicos'),
    path('mapa/', views.mapa_view, name='mapa'),
]
