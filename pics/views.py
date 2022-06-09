from django.shortcuts import render,redirect
from .models import Category,photo
# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    photos = photo.objects.all()
    context = {'categories':categories,'photos':photos}
    return render (request,'pics/gallery.html', context)


def viewphoto(request, pk):
    photos = photo.objects.get(id=pk)
    return render (request,'pics/photo.html',{'photo':photo})


def addphoto(request):
    categories = Category.objects.all()
    
    
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')
    
    context = {'categories':categories,}
    return render (request,'pics/add.html', context)
