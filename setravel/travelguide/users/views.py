from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

from .models import FavPlaces, UserResetPassInfo
from .forms import UserInformationForm, ChangePasswordForm


def login(request):
    if request.POST.get('username', None) is not None:
        username = request.POST.get('username', None).strip()
        password = request.POST.get('password', None).strip()
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Login successful')
            return redirect('mainpage')
        else:
            messages.add_message(request, messages.ERROR, 'Login failed')
    return render(request, 'user/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', None).strip()
        first_name = request.POST.get('first_name', None).strip()
        last_name = request.POST.get('last_name', None).strip()
        email = request.POST.get('email', None).strip()
        password = request.POST.get('password', None).strip()
        question = request.POST.get('question', None).strip()
        answer = request.POST.get('answer', None).strip()
        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.WARNING,
                                 'Username already exists')
        else:
            if User.objects.filter(email=email).exists():
                messages.add_message(
                    request, messages.WARNING, 'Email already exists')
            else:
                User.objects.create_user(
                    first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                user = User.objects.get(username=username)
                UserResetPassInfo.objects.create(
                    user=user, resquestion=question, resanswer=answer)
                messages.add_message(
                    request, messages.SUCCESS, 'Created user successfully')
                return login(request)
    return render(request, 'user/register.html')


def logout(request):
    if User.is_authenticated:
        auth.logout(request)
        return redirect('index')
    else:
        return login(request)


def resetpassword(request):
    if request.method == 'POST':
        if request.POST.get('step') == "1":
            return render(request, 'user/reset.html')
        elif request.POST.get('step') == "2":
            email = request.POST.get('email')
            if User.objects.filter(email=email):
                user = User.objects.get(email=email)
                respass = UserResetPassInfo.objects.get(user=user)
                context = {
                    'respass': respass,
                    'email': email, 
                }
                return render(request, 'user/check.html', context)
            else:
                messages.add_message(request, messages.ERROR, 'Wrong email')
                return render(request, 'user/reset.html')
        elif request.POST.get('step') == "3":
            email = request.POST.get('email')
            answer = request.POST.get('answer')
            respass = request.POST.get('respass')
            print(respass.resanswer)
            if respass.resanswer == answer:
                return render(request, 'user/newpass.html', {'email': email})
            else:
                messages.add_message(request, messages.ERROR, 'Wrong answer')
                context = {
                    'respass': respass,
                    'email': email, 
                }
                return render(request, 'user/check.html', context)
        elif request.POST.get('step') == "4":
            email = request.POST.get('email')
            newpassword = request.POST.get('newpassword')
            renewpassword = request.POST.get('renewpassword')
            if newpassword == renewpassword:
                user = User.objects.get(email=email)
                User.set_password(user, newpassword)
                User.save(user, force_update=True)
                messages.add_message(
                    request, messages.SUCCESS, 'Reset password')
                return render(request, 'user/login.html')
            else:
                messages.add_message(
                    request, messages.ERROR, 'New Passwords are not same.')
                return render(request, 'user/newpass.html', {'email': email})
    else:
        return login(request)


def userinfo(request):
    if User.is_authenticated:
        userid = request.POST.get('userid')
        user = User.objects.get(id=userid)
        question = UserResetPassInfo.objects.get(user=user)
        initial_data_info = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'resquestion': question.resquestion,
        }
        form1 = UserInformationForm(initial=initial_data_info)
        form2 = ChangePasswordForm(initial=initial_data_info)
        context = {
            'form1': form1,
            'form2': form2,
        }
        return render(request, 'user/userinfo.html', context)
    else:
        return login(request)


def upinfo(request):
    if User.is_authenticated:
        if request.method == 'POST':
            form = UserInformationForm(request.POST)
            if form.is_valid():
                User.objects.update(**form.cleaned_data)
                messages.add_message(request, messages.SUCCESS, 'Update info')
            return userinfo(request)
    else:
        return login(request)


def uppass(request):
    if User.is_authenticated:
        if request.method == 'POST':
            userid = request.POST.get('userid')
            user = User.objects.get(id=userid)
            question = UserResetPassInfo.objects.get(user=user)
            answer = request.POST.get('resanswer')
            newpassword = request.POST.get('newpassword')
            renewpassword = request.POST.get('renewpassword')
            if question.resanswer == answer:
                if renewpassword != newpassword:
                    messages.add_message(
                        request, messages.ERROR, 'New Passwords are not same.')
                else:
                    User.set_password(user, newpassword)
                    User.save(user, force_update=True)
                    auth.login(request, user)
                    messages.add_message(
                        request, messages.SUCCESS, 'Update password')
            else:
                messages.add_message(
                    request, messages.ERROR, 'Wrong answer.')
        return userinfo(request)
    else:
        return login(request)
