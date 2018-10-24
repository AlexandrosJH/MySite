from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hellow world")

def detail(request, question_id):
    return HttpResponse('You looking at question %s.' % question_id)

def results(request, question_id):
    return HttpResponse('You looking at the result question %s.' % question_id)

def vote(request, question_id):
    return HttpResponse('You voting on question %s.' % question_id)