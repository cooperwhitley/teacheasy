from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from main_app.models import Course, Post, Comment, Assignment, Submission
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import uuid, boto3, os

# Create your views here.

# Home view
def home(request):
    return render(request, 'home.html')

# About view
def about(request):
    return render(request, 'about.html')

# Course Index
class CourseList(ListView):
    model: Course
    template_name = 'courses/index.html'

# CourseDetail
class CourseDetail(DetailView):
    model: Course
    template_name = 'courses/detail.html'

# CourseCreate
class CourseCreate(CreateView):
    model = Course
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

# Course Update
class CourseUpdate(UpdateView):
    model = Course
    fields = '__all__'

# Course Delete
class CourseDelete(DeleteView):
    model = Course
    success_url = '/courses'