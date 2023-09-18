from django.urls import path
from . import views

urlpatterns = [
    # Route for home page
    path('', views.home, name='home'),
    # Route for about page
    path('about/', views.about, name='about'),
    # Route for class index
    # Route for class details
    # Route for create class
    # Route for update class
    # Route for delete class
]