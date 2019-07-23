from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Myuser

# Create your views here.

def home(request):
    myuser_id = request.session.get('user_id')
    myuser = None
    if myuser_id:
        myuser = Myuser.objects.get(pk=myuser_id)

    return render(request ,'home.html',{
        'user': myuser
    })

def register(request):
    if request.method == 'POST':
        myuser = Myuser()

        if 'username' not in request.POST:
            pass
        
        if 'password' not in request.POST:
            return redirect('/register/')

        myuser.username = request.POST.get('username')
        myuser.password = make_password(request.POST.get('password' ))
        myuser.save()

        return redirect('/')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            myuser = Myuser.objects.get(username = username) 
        except Myuser.DoesNotExist:
            return redirect('/login/')
        
        if check_password(password, myuser.password):
            request.session['username'] = myuser.username
            request.session['user_id'] = myuser.id

            return redirect('/')

    return render(request, 'login.html')

def logout(request):
    if 'user_id' in request.session:
        del(request.session['user_id'])

    return redirect('/')