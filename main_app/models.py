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


class Class(models.Model):
    name = models.CharField(max_length=50)
    enrollment_cap = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    days = models.ManyToManyField(DaysOfTheWeek)
    subject = models.CharField(max_length=4, choices=SUBJECTS, default=SUBJECTS[0][0])

    def __str__(self):
        return f'Course {self.name}, {self.start_date}-{self.end_date}'
