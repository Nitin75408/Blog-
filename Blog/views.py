from django.http import HttpResponse
from django.shortcuts import render
from Blog.models import Post,Category

# Create your views here.
def home(request):
    #load all the post from db(10)
    posts = Post.objects.all()[:11]

    #load all the category from db
    cats = Category.objects.all()

    data = {
    'posts': posts ,

     'cats' : cats
    }
    return  render(request,'home.html',data)

def post(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return  render(request,'posts.html',{'post':post, 'cats':cats})