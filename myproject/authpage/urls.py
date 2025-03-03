from django.urls import path
from authpage import views 

urlpatterns = [
    path("cnfrm/", views.cnfrm),
    path("cnfrm1/", views.cnfrm1),
    path("lockscreen/", views.lockscreen),
    path("lockscreen2/", views.lockscreen2),
    path("login_2/", views.login_2),
    path("logout_2/", views.logout_2),
    path("recoverpw_2/", views.recoverpw_2),
    path("recoverpw/", views.recoverpw),
    path("register_2/", views.register_2),
    path("signin_signup2/", views.signin_signup_2),
    path("signin_signup/", views.signin_signup),

]