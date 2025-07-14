from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroForm
from .models import Profissional

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('servicos')
        else:
            return render(request, 'core/login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'core/login.html')

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'core/register.html', {'form': form})

def servicos_view(request):
    return render(request, 'core/servicos.html')

def mapa_view(request):
    servico = request.GET.get('servico', '')
    profissionais = Profissional.objects.filter(tipo_servico=servico)
    return render(request, 'core/mapa.html', {'servico': servico, 'profissionais': profissionais})
