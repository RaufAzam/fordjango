from django.urls import path
from maps import views 

urlpatterns = [
    path("google/", views.google),
    path("mapael/", views.mapael),
    path("vector/", views.vector),
    
]