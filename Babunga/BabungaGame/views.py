from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    print(reverse("index"))
    return render(request,'index.html')

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            print(user.username)
            print(user.password)
            user = authenticate(username = user.username,password = user.password)
            print(user)
            return JsonResponse({"status":"success"})
        else:
            return JsonResponse({"status": "failed"})
    else:
        return JsonResponse({"status":"failed"})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return  HttpResponse("Konto nieaktywne")
        else:
            print("Username: {} password {}".format(username,password))
            failed = True
            return render(request,'login.html',context={"failed":failed})
    else:
        return render(request,'login.html')



