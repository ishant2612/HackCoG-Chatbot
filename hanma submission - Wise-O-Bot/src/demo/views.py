from django.shortcuts import render
from .chat_gpt import get_chat_response
from django.http import HttpResponse
import json
from django.http import JsonResponse
import openai


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

# def form(request):
#     return render(request, 'form.html')

def chat_gpt(request):
    
    response = get_chat_response(request.GET.get('prompt'))

    return HttpResponse(json.dumps(response), content_type='application/json')

def form(request):
    x1 = request.POST.get("r1")
    x2 = request.POST.get("r2")
    x3 = request.POST.get("r3")
    r = get_chat_response(" Hey my statement for decision is {}, my options and choice are {} and i want specific one optimal and effective choice ,{} this is additional information and you have to give reply as decision , pros of secision and cons of decision".format(x1,x2,x3))
    return render(request,"form1.html",{'r':r})