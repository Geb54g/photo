from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render (request,'pics/gallery.html')


def viewpic(request,pk):
    return render (request,'pics/pics.html')


def addpic(request):
    return render (request,'pics/add.html')
