from django.db import models
from django.urls import reverse
from datetime import date


SUBJECTS = (
    ('SCI', 'Science'),
    ('HIS', 'History'),
    ('SOC', 'Social Studies'),
    ('MATH', 'Mathematics'),
    ('ENG', 'English'),
    ('CS', 'Computer Science'),
    ('ART', 'Arts')
)


# Create your models here.

class DaysOfTheWeek(models.Model):
    day = models.CharField(max_length=10)
    
    def __str__(self):
        return self.day


class Course(models.Model):
    name = models.CharField(max_length=50)
    enrollment_cap = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    # to facilitate schedules being multiple days of the week we utilized a separate object to store dates with a many to many relationship between classes and days
    days = models.ManyToManyField(DaysOfTheWeek)
    subject = models.CharField(max_length=4, choices=SUBJECTS, default=SUBJECTS[0][0])
    require_password = models.BooleanField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'Course {self.name}, {self.start_date}-{self.end_date}'


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'Post {self.title} from course {self.course}'
    
# comments model
class Comment(models.Model):
    body = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment {self.body} on post {self.post}'

# assignments
class Assignment(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'Assignment {self.title} for course {self.course}'

# submissions

class Submission(models.Model):
    url = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    def __str__(self):
        return f'Submission file {self.url} for assignment {self.assignment}'