from django.http import HttpResponse
from django.shortcuts import render

#index_age, index_name, index_groupe, index_common


def index_name(request):
    return HttpResponse("Я Иван Левченко")

def index_age(request):
    return HttpResponse("Мне 20 лет")


def index_groupe(request):
    return HttpResponse("Моя группа: БИН-22-2")

def index_common(request):
    return HttpResponse("Я Иван Левченко. Мне 20 лет. Моя группа: БИН-22-2")
