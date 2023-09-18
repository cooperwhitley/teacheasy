from django.shortcuts import render

# Import the Class model
from .models import Class

# Dummy Data
Classes = [
    {
        'classname': 'John',
        'teacher':'Jane Smith',
        'studentsenrolled':'15',

    }
]

# Create your views here.
# Home view
def home(request):
    return render(request, 'home.html')
# About view
def about(request):
    return render(request, 'about.html')
# Index view for courses
def classes_index(request):
    classes = Class.objects.all()
    return render(request, 'classes/index.html', { 'classes': classes })
# Details for a single class
# classCreate view
# updateView for a single class
# deleteView for a single class
