from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def login(request):

    if request.method == 'POST':
        signInusername = request.POST['u1']
        signInpassword= request.POST['p1']
        user = authenticate(request, username = signInusername, password=signInpassword)
        return render(request, 'core/index.html')
    else:
        return render(request, 'core/login.html')


def profile(request):
    return render(request, 'core/profile.html')
