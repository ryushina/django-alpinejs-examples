from django.http import JsonResponse
from django.shortcuts import render
import time


# Create your views here.
def index(request):
    return render(request, "index.html", {})


def people(request):
    people = [
        {"name": "Mark", "image": "https://via.placeholder.com/150"},
        {"name": "Jeff", "image": "https://via.placeholder.com/150"},
    ]
    return JsonResponse(people, safe=False)
