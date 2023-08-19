from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, "home/index.html",context)



