from django.shortcuts import render
from .models import Profile, Skill, Project, Education, Contact


def home(request):
    context = {
        'profile':   Profile.objects.first(),
        'skills':    Skill.objects.all(),
        'projects':  Project.objects.all(),
        'education': Education.objects.all(),
        'contact':   Contact.objects.first(),
    }
    return render(request, 'home.html', context)
