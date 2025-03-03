from django.urls import path
from calendr import views 

urlpatterns = [
    path("calendar/", views.calendar),
    path("newc/", views.newc),
]