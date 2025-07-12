from django.shortcuts import render, get_object_or_404
from .models import Project
from django.core.paginator import Paginator
from .utils import get_github_project_stats


def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_list(request):
    project_list = Project.objects.all().order_by('-created_at')
    paginator = Paginator(project_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'projects/project_list.html', {'page_obj': page_obj})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    # Fetch live GitHub stats (if project has a repo URL)
    github_stats = {}
    if project.repo_url:
        github_stats = get_github_project_stats(project.repo_url)
    
    project_details = {
        'github_stats': github_stats,
        'technologies_used': project.technologies.split(',') if project.technologies else [],
        'deployment_status': 'Live' if project.is_live else 'In Progress',
    }
    
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'project_details': project_details,
    })


