# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import date

from .models import *


def register_institute(request):
    if request.method == 'POST':

        form = InstituteForm(request.POST, request.FILES)
        password = request.POST['password']
        username = request.POST['email']
        user = User(email=username, password=password, is_institute=1, username=username)
        user.save()
        if form.is_valid():
            institute = Institute(institution_name=form.cleaned_data['institution_name'],
                                  address=form.cleaned_data['address'],
                                  level=form.cleaned_data['level'], website=form.cleaned_data['website'],
                                  photo=form.cleaned_data['photo'], user=user)
            institute.save()

        auth.login(request, user)
        return render(request, 'institute/dashboard.html')

    return render(request, '/institute-dashboard')


def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            password = request.POST['password']
            username = request.POST['email']
            user = User(email=request.POST['email'], is_student=1, password=password, username=username,
                        first_name=request.POST['first_name'], last_name=request.POST['last_name'])
            user.save()
            student = Student(gender=form.cleaned_data['gender'], DOB=form.cleaned_data['DOB'],
                              phone_number=form.cleaned_data['phone_number'], level=form.cleaned_data['level'],
                              father_email=form.cleaned_data['father_email'], photo=form.cleaned_data['photo'],
                              mother_email=form.cleaned_data['mother_email'], user=user,
                              father_name=form.cleaned_data['father_name'],
                              father_phone=form.cleaned_data['father_phone'],
                              mother_name=form.cleaned_data['mother_name'],
                              mother_phone=form.cleaned_data['mother_phone'])
            student.save()
            auth.login(request, user)

    return render(request, '/student-dashboard')


def login(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.filter(username=username, password=password).first()
            print(user)
            if user is not None:
                print('bhakoho?')
                auth.login(request, user)
                if user.is_institute:
                    return render(request, 'institute/dashboard.html')
                else:
                    return render(request, '/student-dashboard/')
        except:
            print('hey?')
            messages.error(request, 'Username or password didn\'t match.')


@login_required(login_url="/")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url="/")
def student_dashboard(request):
    institute = Institute.objects.all()
    return render(request, 'student/dashboard.html', {'institute': institute})


@login_required(login_url="/")
def institute_dashboard(request):
    institute = Student.objects.all()
    return render(request, 'institute/dashboard.html', {'institute': institute})


def institute_profile(request, id):
    institute = Institute.objects.get(id=id)
    return render(request, 'institute/profile.html', {'institute': institute})


def apply(request):
    user = User.objects.get(username=request.POST['user'])
    student = Student.objects.get(user=user)
    institute = Institute.objects.get(id=request.POST['institute'])
    applicants = Applicants(student=student, institute=institute, date=date.today())
    applicants.save()
    return HttpResponseRedirect("/institute/profile/"+request.POST['institute'])
# @login_required(login_url="/")
# def home(request):
#     return render(request, 'app1/home.html')
#
# # @login_required(login_url="/")
# # def welcome(request):
# #     return render(request, 'app1/welcome.html')
