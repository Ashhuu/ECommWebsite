from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductDetails
# Create your views here.

def Homepage(request):
    html = "This is product one"
    product = ProductDetails.objects.all()
    return render(request, 'web/homepage.html', {'html': html, 'products':product})
