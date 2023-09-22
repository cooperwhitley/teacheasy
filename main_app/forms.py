from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Comment, Post, Assignment, Course

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body',)

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ('title', 'body', 'due_date',)


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'start_date', 'end_date', 'days', 'subject',)       

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password')