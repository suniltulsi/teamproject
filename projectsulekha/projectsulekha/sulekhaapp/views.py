from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

# Create your views here.
def login(request):
	return HttpResponse("hi")