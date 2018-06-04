from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Course, Enrollment
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

@login_required
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user, course=course
    )
    if created:
        enrollment.activate()
        messages.success(request, "Inscrição realizada com sucesso!")
    else:
        messages.info(request, "Você já está inscrito no curso")
    
    return redirect("accounts:dashboard")

@login_required
def undo_enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
    context = {}
    if request.POST:
        enrollment.delete()
        messages.success(request, "Sua inscrição foi cancelada com sucesso")
        return redirect("accounts:dashboard")
    context["course"] = course
    return render(request, "courses/undo_enrollment.html", context)

@login_required
def announcements(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if not request.user.is_staff:
        enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
        if not enrollment.is_approved():
            messages.error(request, "A sua inscrição está pendente!")
            return redirect("accounts:dashboard")
    context = {
        "course": course
    }
    return render(request, "courses/announcements.html", context)
    

