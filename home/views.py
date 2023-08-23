from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from .models import User
from .forms import UserForm 

# Create your views here.
def home(request):
    context = {}
    return render(request, "home/home.html", context)

def signin(request):
    if request.method == 'GET':
        context = {'form': AuthenticationForm}
        return render(request, 'auth/signin.html', context)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context = {'form': AuthenticationForm, 'error' : 'El usuario o la contraseña son incorrectos'}
            return render(request, 'auth/signin.html', context)
        else:
            login(request, user)
            return redirect('home:home')

def signout(request):
    logout(request)
    return redirect('home:home')
""" def signup(request):
    signup_form = SignUpForm()
    context = {'form': signup_form}
    return render(request, 'signup.html', context) """

def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, "user/index.html", context)

def user_create(request):
    if request.method == 'GET':
        user_form = UserForm()
        context = {'user_form': user_form}
        return render(request, "user/create.html", context)
    else:
        return HttpResponse('Método no soportado')

def user_store(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('home:users')
        else:
            return HttpResponse('El formulario no es válido')
    else:
        return HttpResponse('Método no soportado')




