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

    def __str__(self):
        return f'Course {self.name}, {self.start_date}-{self.end_date}'


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'Post {self.title} from course {self.course}'
    
# comments model

# assignments

# submissions model