from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def Register_user(request):
    if request.method == 'POST':
        username = request.POST.get('user')

        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Not correct username')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This mail already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                email=email, password=password)
                user.save()
            return redirect('book_list')
        else:
            messages.info(request, 'This password not matching ')
            return redirect('register')
    return render(request, 'athentic/register.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('listbook')
        else:
            messages.info(request, 'please enter correct password')
            return redirect('login')

    return render(request, 'athentic/login.html')


def logOut(request):
    auth.logout(request)
    return redirect('login')


def HomePage(request):
    return render(request, 'athentic/home.html')





