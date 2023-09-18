from django.urls import path
from . import views

urlpatterns = [
    # Home url
    path('', views.home, name='home'),
    # About url
    path('about/', views.about, name='about'),
    # Course urls
    path('courses/', views.CourseList.as_view(), name='courses_index'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='courses_detail'),
    path('courses/create/', views.CourseCreate.as_view(), name='courses_create'),
    path('courses/<int:pk>/update', views.CourseUpdate.as_view(), name='courses_update'),
    path('courses/<int:pk>/delete', views.CourseDelete.as_view(), name='courses_delete'),
    # Post Views
    path('posts/', views.PostList.as_view(), name='posts_index'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='posts_detail'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name='posts_delete'),
    # Comment Views
    # Assignment Views
    path('assignments/', views.AssignmentList.as_view(), name='assignments_index'),
    path('assignments/<int:pk>/', views.AssignmentDetail.as_view(), name='assignments_detail'),
    path('assignments/create/', views.AssignmentCreate.as_view(), name='assignments_create'),
    path('assignments/<int:pk>/update', views.AssignmentUpdate.as_view(), name='assignments_update'),
    path('assignments/<int:pk>/delete', views.AssignmentDelete.as_view(), name='assignments_delete'),
    # Submission Views
]