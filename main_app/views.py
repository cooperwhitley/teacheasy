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
from .forms import CommentForm
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
    model = Course
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()

class CourseDetail(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    pk_url_kwarg = 'course_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_in_course'] = self.object.students.filter(id=self.request.user.id).exists()
        return context

class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'courses/create.html'    
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    template_name = 'courses/update.html'     
    fields = '__all__'

class CourseDelete(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'courses/delete.html'
    success_url = '/courses'

@login_required
def owned_courses(request):
    user = request.user
    owned_courses = Course.objects.filter(user=user)

    context = {
        'owned_courses': owned_courses,
    }

    return render(request, 'courses/owned_courses.html', context)
    

@login_required
def enrolled_courses(request):
    user = request.user
    enrolled_courses = user.course_set.all() 

    context = {
        'enrolled_courses': enrolled_courses,
    }

    return render(request, 'courses/enrolled_courses.html', context)

@login_required
def join_course(request, course_id):
    Course.objects.get(id=course_id).students.add(request.user)

    return redirect('courses_detail', course_id=course_id)

@login_required
def leave_course(request, course_id):
    Course.objects.get(id=course_id).students.remove(request.user)

    return redirect('courses_detail', course_id=course_id)

# Post Views
class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/index.html'

@login_required
def posts_detail(request, post_id):
    return render(request, 'posts/detail.html', {
        'post': Post.objects.get(id=post_id),
        'comment_form': CommentForm()
    })

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

@login_required
def add_comment(request, post_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post_id = post_id
        new_comment.user_id = request.user.id
        new_comment.save()

    return redirect('posts_detail', post_id=post_id)

def delete_comment(request, post_id, comment_id):
    Comment.objects.get(id=comment_id).delete()
    return redirect('posts_detail', post_id=post_id)


# Assignment Views

class AssignmentDetail(LoginRequiredMixin, DetailView):
    model = Assignment
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

@login_required
def submission_detail(request, assignment_id, submission_id):
    return render(request, 'submissions/detail.html', {
        'assignment': Assignment.objects.get(id=assignment_id),
        'submission': Submission.objects.get(id=submission_id)
    })

@login_required
def upload_submission(request, assignment_id):
    submission_file = request.FILES.get('submission-file', None)
    if submission_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + submission_file.name[submission_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(submission_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Submission.objects.create(url=url, assignment_id=assignment_id, user=request.user, comment=request.POST.get('comment', ' '))
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
            print(os.environ['S3_BUCKET'])
    return redirect('assignments_detail', pk=assignment_id)