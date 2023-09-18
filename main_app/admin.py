from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DaysOfTheWeek, Course, Post, Comment, Assignment, Submission, User

# Register your models here.
admin.site.register(DaysOfTheWeek)
admin.site.register(Course)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(User, UserAdmin)