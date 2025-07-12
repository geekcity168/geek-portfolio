from django.shortcuts import render
from projects.models import Project
from blog.models import Post

def home(request):
    # Get featured projects (you can add a 'featured' field to Project model)
    projects = Project.objects.all().order_by('-created_at')[:6]
    
    # Get recent blog posts
    posts = Post.objects.all().order_by('-created_at')[:3]
    
    context = {
        'projects': projects,
        'posts': posts,
    }
    return render(request, 'core/home.html', context)
