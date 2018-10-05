from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_num_list(request):
    num = []
    for i in range(10):
        num.append(i)
    return JsonResponse({'data': num})

def get_obj(request):
    obj = {
        "a": 1,
        "b": 2,
        "c": 3
    }
