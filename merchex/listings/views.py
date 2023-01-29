from django.shortcuts import render
from listings.models import Band, Listing
# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands":bands})

def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", {"listings":listings})

def contact_us(request):
    return render(request, "listings/contact.html")
    
def about(request):
    return render(request, "listings/about.html")
