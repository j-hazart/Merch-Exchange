from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello django</h1>')
def listings(request):
    return HttpResponse('<h1>Listings</h1><p>En construction</p>')
def contact_us(request):
    return HttpResponse('<h1>Contact Us</h1><p>En construction</p>')