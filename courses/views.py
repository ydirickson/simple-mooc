from django.shortcuts import render, get_object_or_404

from .models import Course

def courses(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request,"courses/courses.html", context)

def detail(request, slug):
    context = {
        "course":get_object_or_404(Course,slug=slug)
    }
    return render(request,"courses/course.html", context)