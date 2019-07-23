from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Board

# Create your views here.

def board_list(request):
    boards = Board.objects.all().order_by('-id') 
    page = int(request.GET.get('p',1)) #get은 딕셔너리 변수 p라는 키로 1값을 받는다.
    paginator = Paginator(boards, 3)
    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})
    
