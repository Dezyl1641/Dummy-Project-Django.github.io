from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Post
from django.views.generic import ListView, DetailView, CreateView


def home(request):
    if request.method=="POST":
        fullname = request.POST.get('fullname')
        company = request.POST.get('company')
        position = request.POST.get('position')
        ins = Post(fullname=request.user, company=company, position=position)
        ins.save()
    
    context = {
        'posts':Post.objects.all()
        
        }
    
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name='posts'
    ordering = ['-date_posted']
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    
    

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/form.html'
    fields= ['company', 'position', 'content' ]


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})