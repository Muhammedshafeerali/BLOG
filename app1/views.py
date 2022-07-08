from django.shortcuts import render
from .models import Blog
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request,"home.html")

def newPost(request):
    if request.method == "POST":
        blog=Blog.objects.create(heading=request.POST.get('heading'),Category=request.POST.get('Category'),tags=request.POST.get('Tags'),content=request.POST.get('content'))
        blog.save()
        msg = "Blog has been saved. "
        messages.success(request, msg)
    return render(request,"newpost.html")

def viewPost(request):
    blogs=Blog.objects.all()
    return render(request,"viewblog.html",{'blogs':blogs})


def getcategory(request):
    categ=request.GET.get('categ')
    try:
        print(categ)
        blogs=list(Blog.objects.filter(Category=categ).values('heading','content'))
    except:
        blogs=[]

    print(blogs)
    return JsonResponse({'success': True, 'blogs': blogs})
    
    