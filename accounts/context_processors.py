from courses.models import Enrollment

def enrollments(request):
    if hasattr(request, "user"):
        enrollments = Enrollment.objects.filter(user=request.user)
    else:
        enrollments = []
    return {
        "enrollments":enrollments
    }