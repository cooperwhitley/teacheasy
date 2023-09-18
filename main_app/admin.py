from django.contrib import admin
from .models import DaysOfTheWeek, Course, Post, Comment, Assignment, Submission

# Register your models here.
admin.site.register(DaysOfTheWeek)
admin.site.register(Course)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Assignment)
admin.site.register(Submission)