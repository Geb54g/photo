from django.shortcuts import render
from .models import category,photo
# Create your views here.
def gallery(request):
    return render (request,'pics/gallery.html')


def viewphoto(request, pk):
    return render (request,'pics/photo.html')


def addphoto(request):
    return render (request,'pics/add.html')
