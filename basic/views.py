from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def detail(request, question_id):
    return HttpResponse(str(question_id)+"Hello, world. You're at the polls index.")
