from django.urls import path
from . import views

urlpatterns = [
    # Home url
    path('', views.home, name='home'),
    # About url
    path('about/', views.about, name='about'),
    # Course urls
    path('courses/', views.CourseList.as_view(), name='courses_index'),
    path('courses/<int:course_id>/', views.CourseDetail.as_view(), name='courses_detail'),
    path('courses/create/', views.CourseCreate.as_view(), name='courses_create'),
    path('courses/<int:pk>/update', views.CourseUpdate.as_view(), name='courses_update'),
    path('courses/<int:pk>/delete', views.CourseDelete.as_view(), name='course_delete'),
    # Post Views
    # Comment Views
    # Assignment Views
    # Submission Views
]