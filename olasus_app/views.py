from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    return render(request, 'olasus_app/index.html')

def modulo_acs(request):
    # Redireciona o usuário para a página 'modulo_acs.html'
    return redirect('olasus_app:modulo_acs')

def login_view(request):
    if request.method == 'POST':
        # Renomeie a variável login para evitar conflitos
        user_login = request.POST['login']
        password = request.POST['password']
        print(f'Login: {user_login}, Password: {password}')
        # Autentique o usuário
        user = authenticate(request, username=user_login, password=password)

        if user is not None:
            # Login bem-sucedido
            print(f'User authenticated: {user}')
            login(request, user)
            return redirect('modulo_acs')  # Alteração feita aqui
        else:
            # Login falhou
            print('Authentication failed')
            messages.error(request, 'Credenciais inválidas')
            return redirect('index')  # Corrija para redirecionar para o index do olasus_app

    return render(request, 'olasus_app/modulo_acs.html')
