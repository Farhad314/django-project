from django.shortcuts import render

from .models import Post, Slider
# Create your views here.
def carou(request):
    posts = Post.objects.all()
    sliders = Slider.objects.all()
    context = {
        "posts": posts,
        "sliders":sliders

    }
    return render(request, 'carousel/index.html', context)