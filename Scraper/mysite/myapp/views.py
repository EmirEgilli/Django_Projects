from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link
from django.db import connection

# Create your views here.

def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site', '')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:   
        data = Link.objects.all()

    return render(request, 'myapp/result.html', {'data': data})

def clear(request):
    Link.objects.all().delete()
    
    # Reset the primary key sequence
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='myapp_link'")

    return redirect('result')  # Assuming 'result' is the name of the URL pattern for the result view
