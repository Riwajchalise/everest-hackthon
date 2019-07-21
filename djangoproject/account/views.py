# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import date

from django.core.mail import send_mail

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
                                  address=form.cleaned_data['address'], phone_number=form.cleaned_data['phone_number'],
                                  level=form.cleaned_data['level'], website=form.cleaned_data['website'],
                                  photo=form.cleaned_data['photo'], user=user)
            institute.save()

        auth.login(request, user)
        messages.success(request, 'Institute has been registered.')

        return render(request, 'institute/confirmation.html')

    return render(request, '/')


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
            messages.success(request, 'Student has been registered.')

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
                    return HttpResponseRedirect('/institute-dashboard')

                else:
                    return HttpResponseRedirect('/student-dashboard')
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
    # print(request.user.username)
    # u = User.objects.get(username=request.user.username)
    # print(type(u))
    print(request.user)
    i = Institute.objects.get(user=request.user)
    print(i)
    institute = Applicants.objects.filter(institute=i)
    return render(request, 'institute/dashboard.html', {'institute': institute})


def institute_profile(request, id):
    user = User.objects.get(id=id)
    institute = Institute.objects.get(user=user)
    admission=Admission.objects.all()
    return render(request, 'institute/profile.html', {'institute': institute,'admission':admission})


def student_profile(request, id):
    profile = User.objects.get(id=id)
    student = Student.objects.get(user=profile)
    return render(request, 'student/profile.html', {'student': student})


def apply(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        student = Student.objects.get(user=user)
        institute = Institute.objects.get(id=request.POST['institute'])
        applicants = Applicants(student=student, institute=institute, date=date.today())
        applicants.save()
        # messages.success(request, 'Application submitted!')

        subject = 'Student Application:#' + str(applicants.id)
        subject1 = 'Application token:#' + str(applicants.id)
        html_content1 = '<p> Hello, <br>' + ' Your application token is provided below:' + '<br>' + 'Token:' + str(
            applicants.id) + '<br>For more details visit the website </p>'

        html_content = '<p> Hello, <br>' + ' Details are as follows:' + '<br>' + 'Name:' + user.first_name + user.last_name + '<br>For more details visit the website </p>'
        try:
            send_mail(subject, '', 'shreya998.ss@gmail.com',
                      [institute.user.email],
                      fail_silently=False, html_message=html_content)
            send_mail(subject1, '', 'shreya998.ss@gmail.com',
                      [user.email],
                      fail_silently=False, html_message=html_content1)
            messages.add_message(request, messages.SUCCESS, 'Application submitted successfully!')

        except:
            messages.add_message(request, messages.ERROR, 'Something went wrong, try sending the email again later!')

        return HttpResponseRedirect("/institute/profile/" + request.POST['institute'] + '/')


# @login_required(login_url="/")
# def home(request):
#     return render(request, 'app1/home.html')
#
# # @login_required(login_url="/")
# # def welcome(request):
# #     return render(request, 'app1/welcome.html')


def open_admission(request):
    institute = Institute.objects.get(id=request.POST['institute'])
    admission = Admission(institute=institute, deadline=request.POST['deadline'], status=request.POST['status'])
    admission.save()
    return HttpResponseRedirect("/institute/profile/" + institute.user.id + '/')


def close_admission(requset):
    admission=Admission.objects.get(id=requset.POST['institute'])
    admission.status='Close'
    admission.save()
    return  HttpResponseRedirect("/institute/profile/" + admission.institute.user.id + '/')