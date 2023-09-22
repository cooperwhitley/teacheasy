from django.forms import ModelForm
from .models import Comment, Post, Assignment

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