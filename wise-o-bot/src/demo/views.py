from django.shortcuts import render
from .chat_gpt import get_chat_response
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return render(request, "index.html")

def p1_view(request):
    return render(request, 'p1.html')

def p2_view(request):
    return render(request, 'p2.html')

def p3_view(request):
    return render(request, 'p3.html')

def p4_view(request):
    return render(request, 'p4.html')

def chat_gpt(request):
    
    response = get_chat_response(request.GET.get('prompt'))

    return HttpResponse(json.dumps(response), content_type='application/json')

