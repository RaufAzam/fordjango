from django.shortcuts import render

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
def calendar(request):
    return render(request, "apps/calendar/calendar.html")
def newc(request):
    return render(request, "apps/calendar/newc.html")
def chat(request):
    return render(request, "apps/chat/chat.html")
def company(request):
    return render(request, "apps/companies/companies.html")
def fourzerothree(request):
    return render(request, "403.html")
def fourzerofour(request):
    return render(request, "404.html")
def fivezerozero(request):
    return render(request, "500.html")
def tempbase(request):
    return render(request, "base.html")
def detached_base(request):
    return render(request, "detached_base.html")
def horizontal_base(request):
    return render(request, "horizontal_base.html")
def landing(request):
    return render(request, "landing.html")
def preloader_base(request):
    return render(request, "preloader_base.html")
def two_column_base(request):
    return render(request, "two_column_base.html")
def two_tone_icons_base(request):
    return render(request, "two_tone_icons_base.html")
def vertical_base(request):
    return render(request, "vertical_base.html")
def about(request):
    return render(request, "pages/about.html")
def home(request):
    return render(request, "pages/home.html")
def twocolumnsidebar(request):
    return render(request, "partials/two-column-sidebar.html")
def social_feed(request):
    return render(request, "apps/social/feed.html")
def file_manager(request):
    return render(request, "apps/manager/file-manager.html")
def widgets(request):
    return render(request, "components/widgets.html")