from django.shortcuts import render
from account import views

# Create your views here.
def inactiveaccounts(request):
    return render(request, "account/account_inactive.html")
def base(request):
    return render(request, "account/based.html")
def confirm_email_acc(request):
    return render(request, "account/email_confirm.html")
def login(request):
    return render(request, "account/login.html")
def logout(request):
    return render(request, "account/logout.html")
def passchng(request):
    return render(request, "account/password_change.html")
# Password Changed Done
def passresetdone(request):
    return render(request, "account/password_reset_done.html")
    #Password Reset From Key Done
def prfkdone(request):
    return render(request, "account/password_reset_from_key_done.html")
    # Password Reset From Key
def prfkey(request):
    return render(request, "account/password_reset_from_key.html")
    # Password Reset
def preset(request):
    return render(request, "account/password_reset.html")
    # Password Set
def passset(request):
    return render(request, "account/password_set.html")
    #SignUp Closed
def supclosed(request):
    return render(request, "account/signup_closed.html")
    # SignUp
def sup(request):
    return render(request, "account/signup.html")
    # Verification Sent
def vsent(request):
    return render(request, "account/verification_sent.html")
    # Verified Email Required
def verequired(request):
    return render(request, "account/verified_email_required.html")