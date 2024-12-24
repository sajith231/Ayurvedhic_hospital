from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.



def index(request):
    return render(request, 'app1/index.html')

def about(request):
    return render(request, 'app1/about.html')

def gallery(request):
    return render(request,'app1/gallery.html')