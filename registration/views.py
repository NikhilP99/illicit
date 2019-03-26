from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import CreateUser

## TODO: Add error messages

def reg_forms(request):
    signup_form = CreateUser()
    context = {
    'signup_form':signup_form,
    }
    return render(request,'registration/forms.html',context)


def signup_user(request):
    if request.method == 'POST':
        signup_form = CreateUser(request.POST)
        if signup_form.is_valid():
            blogger = signup_form.cleaned_data
            username = blogger['username']
            password = blogger['password']
            email = blogger['email']
            first_name = blogger['first_name']
            last_name = blogger['last_name']
            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request,user)
            return render(request,'blog/index.html')
        else:
            return HttpResponse('<p>form is not valid</p>')
    else:
        return render(request,'home/index.html')


def login_user(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email=email)

        if not user.check_password(password):
            return HttpResponse('<p>Wrong password...go back</p>')

        login(request,user)

    return render(request,'blog/index.html')


def logout_user(request):
    logout(request)
    return render(request,'home/index.html')
