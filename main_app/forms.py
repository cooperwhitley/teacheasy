from django.forms import ModelForm
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


class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'start_date', 'end_date', 'days', 'subject']        