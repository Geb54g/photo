from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render (request,'pics/gallery.html')


def viewpics(request):
    return render (request,'pics/pics.html')


def addpics(request):
    return render (request,'pics/add.html')
