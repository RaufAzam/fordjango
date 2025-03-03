from django.shortcuts import render

# Create your views here.
def cnfrm(request):
    return render(request, "auth/confirm-email-2.html")
def cnfrm1(request):
    return render(request, "auth/confirm-email.html")
def lockscreen2(request):
    return render(request, "auth/lock-screen-2.html")
def lockscreen(request):
    return render(request, "auth/lock-screen.html")
def login_2(request):
    return render(request, "auth/login-2.html")
def logout_2(request):
    return render(request, "auth/logout-2.html")
def recoverpw_2(request):
    return render(request, "auth/recoverpw-2.html")
def recoverpw(request):
    return render(request, "auth/recoverpw.html")
def register_2(request):
    return render(request, "auth/register-2.html")
def signin_signup_2(request):
    return render(request, "auth/signin-signup-2.html")
def signin_signup(request):
    return render(request, "auth/signin-signup.html")
