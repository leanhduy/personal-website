from django.shortcuts import render
from .models import Project, Profile

# Create your views here.


def index(request):
    """A view to return the index page"""
    profile = Profile.objects.first()
    return render(request, "users/index.html", {"profile": profile})


def single_project(request, id):
    """A view to return a single project"""
    project = Project.objects.get(id=id)
    return render(request, "users/single_project.html", {"project": project})


def personal_projects(request):
    """A view to return all personal projects"""
    projects = Project.objects.filter(project_type="P")
    return render(request, "users/personal_projects.html", {"projects": projects})


def commercial_projects(request):
    """A view to return all commercial projects"""
    projects = Project.objects.filter(project_type="C")
    return render(request, "users/commercial_projects.html", {"projects": projects})


def contact_me(request):
    """A view to return the contact page"""
    return render(request, "users/contact_me.html")
