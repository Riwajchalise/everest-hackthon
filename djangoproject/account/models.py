from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.forms import ModelForm


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_institute = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(null=True, max_length=255)


class Institute(models.Model):
    user = models.OneToOneField(User)
    institution_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    photo = models.FileField(upload_to='institute')
    is_verified=models.BooleanField(default=False)
    phone_number=models.CharField(max_length=10, default=8989898989)
    password = models.CharField(max_length=255, default=123)


class Student(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=12)
    DOB = models.DateField()
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    father_phone = models.CharField(max_length=255)
    mother_phone = models.CharField(max_length=255)
    father_email = models.CharField(max_length=255)
    mother_email = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    photo = models.FileField(upload_to='student')


class InstituteForm(ModelForm):
    class Meta:
        model = Institute
        fields = ['institution_name', 'address', 'level', 'description', 'website', 'photo','phone_number']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['gender', 'DOB', 'phone_number', 'level', 'father_name', 'mother_name', 'father_phone',
                  'mother_phone', 'father_email', 'mother_email', 'photo']


class Applicants(models.Model):
    student = models.ForeignKey(Student)
    institute = models.ForeignKey(Institute)
    date = models.DateField()


class Admission(models.Model):
    institute = models.ForeignKey(Institute)
    status = models.CharField(max_length=255)
    deadline = models.DateField()
