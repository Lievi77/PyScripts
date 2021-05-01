from django.shortcuts import render

from django.http import HttpResponse

#first, indicate what the view should do 
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")