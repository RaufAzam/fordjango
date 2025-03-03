from django.urls import path
from account import views

urlpatterns = [
    path("inactive/",views.inactiveaccounts),
    path("base/", views.base),
    path("confirm_email_acc/", views.confirm_email_acc),
    path("login/", views.login),
    path("logout/", views.logout),
    path("passchange/", views.passchng),
    path("passchangedone/", views.passresetdone),
    path("passset/", views.passset),
    path("prfkdone/", views.prfkdone),
    path("prfkey/", views.prfkey),
    path("preset/", views.preset),
    path("supclosed/", views.supclosed),
    path("sup/", views.sup),
    path("vsent/", views.vsent),
    path("verequired/", views.verequired),
]
