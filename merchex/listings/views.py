from django.shortcuts import render
from listings.models import Band, Listing
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "listings/base.html")

def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands":bands})

def band_detail(request, id):
    try:
        band = Band.objects.get(id=id)
        return render(request, "listings/band_detail.html", {"band":band})
    except:
        return HttpResponse('<h1>404 not found</h1>')

def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings.html", {"listings":listings})

def contact_us(request):
    return render(request, "listings/contact.html")
    
def about(request):
    return render(request, "listings/about.html")