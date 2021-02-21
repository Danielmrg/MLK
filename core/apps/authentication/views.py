from django.shortcuts import render , redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import User
from .decorators import IsAuthenticated
from .forms import LoginForm , SignUpForm
from django.contrib import messages

@IsAuthenticated
def LoginPage(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        if form.LoginUser(request):
            return redirect('home:home')  
    context ={
        "title":"Login",
        "form": form,
    }
        
    return render(request,"Home/forms/SignIn.html",context)


@login_required(login_url="account:Login")
def LogoutPage(request):
    logout(request)
    return redirect('home:home')


@IsAuthenticated
def SignUpPage(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        if form.Save():
            return redirect('home:home')
    context = {
        "title":"Sign Up",
        "form":form
    }
    return render(request,'Home/forms/SignUp.html',context)
