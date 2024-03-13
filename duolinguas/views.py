from django.shortcuts import render
from .models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Perfil
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(
        request,
        'duolinguas/index.html',
    )

def cadastro(request):
    return render(
        request, 
        'duolinguas/cadastroUsuario.html',
    )


def usuarios(request):

    if request.method == 'POST':
    
        username = request.POST.get('nome')
        password = request.POST.get('senha')
        foto = request.FILES.get('foto')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso. Por favor, escolha um diferente.')
            return redirect('/cadastro')  
        
       
        user = User.objects.create(username=username, password=make_password(password))
        user.save()

        novo_usuario = Perfil(usuario=user, foto=foto)
        novo_usuario.save()

        return redirect('index')
    # else:
    #     usuarios = Perfil.objects.all()
    #     return render(request, 'duolinguas/usuarios.html',)

def login(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('duolinguas:index')
        messages.error(request, 'Login inválido')

    return render(
        request,
        'duolinguas/login.html',
        {
            'form': form
        }
    )

def logout(request):
    auth.logout(request)
    return redirect('duolinguas:login')

