from django.shortcuts import render
from .models import Profile

def homepage(request):
    profile = Profile.objects.all()
    context = {
        "profile": profile

    }
    return render(request, 'profile.html', context)