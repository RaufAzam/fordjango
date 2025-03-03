from django.urls import path
from icons import views 

urlpatterns = [
    path("dripicons/", views.dripicons),
    path("feather/", views.feather),
    path("front_awesome/", views.front_awesome),
    path("mdi/", views.mdi),
    path("simple_line/", views.simple_line),
    path("themify/", views.themify),
    path("two_tone/", views.two_tone),
    path("weather/", views.weather),

]