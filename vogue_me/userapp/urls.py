"""
URL configuration for vogue_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views as v

app_name = 'userapp'

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name="app/userapp/login.html"), name="login"),

    path('login/', v.login, name="login"),
    path('pick_style/', v.pick_style, name="pick_style"),
    path('make_avatar/', v.make_avatar, name="make_avatar"),

    path('signup/', v.signup, name="signup"),
    path('check_email', v.check_email_dup, name="check_email_dup"),
    path('verify/<str:encrypted_code>', v.verify_auth_link, name="verify_auth_link"),
]
