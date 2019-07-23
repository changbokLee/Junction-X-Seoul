from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_passowrd, check_password
from .models import Myuser

# Create your views here.
def home(request):
    return HttpResponse('Hello World!')

def register(request):
    if request.method()== 'POST':
        myuser = Myuser()
        
        if 'username' not in request.POST:
            pass
        myuser.username = request.POST.get('username')
        myuser.password = request.POST.get('password')
        myuser.save()

        return redirect('/')

    return render(request, 'register.html')
