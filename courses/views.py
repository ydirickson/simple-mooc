from django.shortcuts import render, get_object_or_404

from .models import Course
from .forms import ContactCourseForm

def courses(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request,"courses/courses.html", context)

def detail(request, slug):
    context = {}
    course = get_object_or_404(Course,slug=slug)
    if request.POST:
        form = ContactCourseForm(request.POST)
        if form.is_valid():
            form.send_email(course)
            context["sent"] = True
            form = ContactCourseForm()
    else:
        form = ContactCourseForm()
    context["form"] = form
    context["course"] = course
    return render(request,"courses/course.html", context)