from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random


class Course(models.Model):
    CATEGORY_OPTIONS = [
        ('video', 'Video'),
        ('document', 'Docucment'),
        ('mcq quiz', 'MCQ Quiz')
    ]
    title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_OPTIONS)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:  # Only send email when the student is created
            password = ''.join(random.choices(
                'abcdefghijklmnopqrstuvwxyz1234567890', k=8))
            print(self.name, self.email)
            message = f'Hello {self.name}, your password for softbenz is: {password}'
            send_mail(
                'Your Password',
                message,
                'noreply@softbenz.com',
                [self.email],
            )
        super().save(*args, **kwargs)

    def get_enrolled_courses(self):
        return Course.objects.filter(enrollment__student=self).values_list('title', flat=True)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.name}-{self.course.title}"
