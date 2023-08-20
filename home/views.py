from django.shortcuts import render
from .models import User

# Create your views here.
def home(request):
    context = {}
    return render(request, "home/home.html",context)

def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, "user/index.html",context)



