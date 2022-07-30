from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Buku

# Create your views here.
def index(request):
    mybook = Buku.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mybook':mybook,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addbook(request):
    a = request.POST['bookName']
    b = request.POST['author']
    c = request.POST['year']
    d = request.POST['publisher']
    e = request.POST['location']
    mybook = Buku(bookName=a, author=b, year=c, publisher=d, location=e)
    mybook.save()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mybook = Buku.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mybook':mybook,
    }
    return HttpResponse(template.render(context, request))

def updatebook(request, id):
  bookName = request.POST['bookName']
  author = request.POST['author']
  year = request.POST['year']
  publisher = request.POST['publisher']
  location = request.POST['location']
  mybook = Buku.objects.get(id=id)
  mybook.bookName = bookName
  mybook.author = author
  mybook.year = year
  mybook.publisher = publisher
  mybook.location = location
  mybook.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):    
  mybook = Buku.objects.get(id=id)
  mybook.delete()
  return HttpResponseRedirect(r 