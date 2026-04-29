from collections import OrderedDict
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
from .models import Profile, Skill, Project, Experience, Certificate


def home(request):
    profile = Profile.objects.first()
    skills = list(Skill.objects.all())
    grouped_skills = OrderedDict()
    for skill in skills:
        grouped_skills.setdefault(skill.category, []).append(skill)
    featured_projects = Project.objects.filter(featured=True).order_by('-date')
    return render(request, 'core/home.html', {
        'profile': profile,
        'skills': skills,
        'grouped_skills': grouped_skills,
        'featured_projects': featured_projects,
    })


def projects(request):
    profile = Profile.objects.first()
    all_projects = Project.objects.all().order_by('-date')
    return render(request, 'core/projects.html', {
        'profile': profile,
        'projects': all_projects,
    })


def project_detail(request, pk):
    profile = Profile.objects.first()
    project = get_object_or_404(Project, pk=pk)
    tools_list = [t.strip() for t in project.tools_used.split(',')]
    return render(request, 'core/project_detail.html', {
        'profile': profile,
        'project': project,
        'tools_list': tools_list,
    })


def about(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'core/about.html', {
        'profile': profile,
        'experiences': experiences,
        'certificates': certificates,
    })


def download_cv(request):
    profile = Profile.objects.first()
    if not profile or not profile.cv_file:
        raise Http404("CV not available.")
    return FileResponse(profile.cv_file.open('rb'), as_attachment=True, filename=profile.cv_file.name.split('/')[-1])
