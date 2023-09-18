from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from main_app.models import Course, Post, Comment, Assignment, Submission
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid, boto3, os

# Create your views here.

# Home view
def home(request):
    return render(request, 'home.html')

# About view
def about(request):
    return render(request, 'about.html')

# Sign Up View

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Course Views
class CourseList(ListView):
    model: Course
    template_name = 'courses/index.html'

class CourseDetail(DetailView):
    model: Course
    template_name = 'courses/detail.html'

class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    fields = '__all__'

class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = '/courses'

# Post Views
class PostList(ListView):
    model: Post
    template_name = 'posts/index.html'

class PostDetail(DetailView):
    model: Post
    template_name = 'posts/detail.html'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = '__all__'

class PostDelete(LoginRequiredMixin, DeleteView):
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

class AssignmentCreate(LoginRequiredMixin, CreateView):
    model = Assignment
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

class AssignmentUpdate(LoginRequiredMixin, UpdateView):
    model = Assignment
    fields = '__all__'

class AssignmentDelete(LoginRequiredMixin, DeleteView):
    model = Assignment
    success_url = '/assignments'

# Submission Views