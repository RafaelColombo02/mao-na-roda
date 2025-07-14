from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('servicos/', views.servicos_view, name='servicos'),
    path('mapa/', views.mapa_view, name='mapa'),
]
