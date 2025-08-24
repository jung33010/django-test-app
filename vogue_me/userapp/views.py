import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from mailapp.models import *
from mailapp.utils import *
from .models import RegisterUserForm


# Create your views here.

def login(request):
    if request.method == "POST":
        pass
    else:
        pass

    return render(request, "app/userapp/login.html")


def pick_style(request):
    return render(request, "app/userapp/pick_style.html")

def make_avatar(request):
    if request.method == "POST":
        pass
    else:
        pass
    return render(request, "app/userapp/make_avatar.html")


def signup(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data["username"]).exists():
                form.add_error("email", "이미 가입된 계정입니다.")
            else:
                user = form.save()
                new_auth = LoginAuth()
                new_auth.user = user
                new_auth.save()
                context = {
                    "auth_link" : "http://"+request.META['HTTP_HOST'] + reverse('userapp:verify_auth_link', kwargs={"encrypted_code" : new_auth.get_encrypted_code()}),
                    "due_time" : new_auth.expires_at.strftime("%Y.%m.%d %H:%M:%S")
                }
                send_mail_with(user.email, "회원가입 본인인증", MailForm.AUTH_LINK, context)
    else:
        form = RegisterUserForm()

    return render(request, "app/userapp/signup.html", {"form":form})

def check_email_dup(request):
    if request.method == "GET": return redirect("mainapp:index")

    data = json.loads(request.body.decode('utf-8'))
    email = data.get("email")
    return JsonResponse({ "already_exist" : User.objects.filter(email=email).exists() })


def verify_auth_link(request, encrypted_code):
    print("code = ", encrypted_code)
    return redirect("userapp:login")
