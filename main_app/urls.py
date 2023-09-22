from django.urls import path
from . import views

urlpatterns = [
    # Home url
    path('', views.home, name='home'),
    # About url
    path('about/', views.about, name='about'),
    # auth urls
    path('accounts/signup/', views.signup, name='signup'),
    
    # Course urls
    path('courses/', views.CourseList.as_view(), name='courses_index'),
    path('courses/<int:course_id>/', views.CourseDetail.as_view(), name='courses_detail'),
    path('courses/create/', views.CourseCreate.as_view(), name='courses_create'),
    path('courses/<int:pk>/update', views.CourseUpdate.as_view(), name='courses_update'),
    path('courses/<int:pk>/delete', views.CourseDelete.as_view(), name='courses_delete'),
    path('courses/<int:course_id>/join/', views.join_course, name='join_course'),
    path('courses/<int:course_id>/leave/', views.leave_course, name='leave_course'),
    path('courses/owned/', views.owned_courses, name='owned_courses'),
    path('courses/enrolled/', views.enrolled_courses, name='enrolled_courses'),
    path('courses/<int:course_id>/add_course/', views.add_course, name='add_course'),

    # Post Views
    path('posts/', views.PostList.as_view(), name='posts_index'),
    path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('posts/<int:course_id>/add_post/', views.add_post, name='add_post'),
    # Comment Views
    path('posts/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('posts/<int:post_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    # Assignment Views
    path('assignments/<int:pk>/', views.AssignmentDetail.as_view(), name='assignments_detail'),
    path('assignments/create/', views.AssignmentCreate.as_view(), name='assignments_create'),
    path('assignments/<int:pk>/update/', views.AssignmentUpdate.as_view(), name='assignments_update'),
    path('assignments/<int:pk>/delete/', views.AssignmentDelete.as_view(), name='assignments_delete'),
    path('assignments/<int:course_id>/add_assignment/', views.add_assignment, name='add_assignment'),
    # Submission Views
    path('assignments/<int:assignment_id>/add_submission/', views.upload_submission, name='upload_submission'),
    path('assignments/<int:assignment_id>/submissions/<int:submission_id>/', views.submission_detail, name='submission_detail'),
]