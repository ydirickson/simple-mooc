from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.models import Group

from .models import Course, Enrollment, Announcement, Comment

@register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "start_date", "created_at")
    search_fields = ("name", "slug")
    prepopulated_fields = {
        "slug":("name",)
    }

admin.site.register([Enrollment, Announcement, Comment])
admin.site.unregister(Group)