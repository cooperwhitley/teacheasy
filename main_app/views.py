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

# Course Views
class CourseList(ListView):
    model: Course
    template_name = 'courses/index.html'

class CourseDetail(DetailView):
    model: Course
    template_name = 'courses/detail.html'

class CourseCreate(CreateView):
    model = Course
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

class CourseUpdate(UpdateView):
    model = Course
    fields = '__all__'

class CourseDelete(DeleteView):
    model = Course
    success_url = '/courses'

# Post Views
class PostList(ListView):
    model: Post
    template_name = 'posts/index.html'

class PostDetail(DetailView):
    model: Post
    template_name = 'posts/detail.html'

class PostCreate(CreateView):
    model = Post
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'

class PostDelete(DeleteView):
    model = Post
    success_url = '/posts'

# Comment Views

# Assignment Views
class AssignmentList(ListView):
    model: Assignment
    template_name = 'assignments/index.html'

class AssignmentDetail(DetailView):
    model: Assignment
    template_name = 'assignments/detail.html'

class AssignmentCreate(CreateView):
    model = Assignment
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

class AssignmentUpdate(UpdateView):
    model = Assignment
    fields = '__all__'

class AssignmentDelete(DeleteView):
    model = Assignment
    success_url = '/assignments'

# Submission Views