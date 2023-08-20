from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm

# Create your views here.
def home(request):
    context = {}
    return render(request, "home/home.html",context)

def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, "user/index.html",context)

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




