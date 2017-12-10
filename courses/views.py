from django.shortcuts import render

from .models import Course

def courses(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request,"courses/courses.html",context)