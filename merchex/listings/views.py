from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello django</h1>
        <p>Mes groupes préférés sont :</p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)
def listings(request):
    return HttpResponse('<h1>Listings</h1><p>En construction</p>')
def contact_us(request):
    return HttpResponse('<h1>Contact Us</h1><p>En construction</p>')