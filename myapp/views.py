from django import http
from django.shortcuts import redirect, render
from .models import UrlShortner
from django.http import HttpResponse
import random
import string

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        short_url = ''.join(random.choices(string.ascii_lowercase, k=5))
        UrlShortner(long_url=link, short_url=short_url).save()
        return render(request, 'myapp/home.html', {'short_url': short_url})
    else:
        return HttpResponse('some error occurs') 
    
def token(request, token):
    link = UrlShortner.objects.get(short_url=token)
    return redirect(link.long_url)