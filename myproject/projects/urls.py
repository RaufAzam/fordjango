from django.urls import path
from projects import views

urlpatterns = [
path("proj_create/", views.proj_create),
    path("proj_detail/", views.proj_detail ),
    path("proj_list/", views.proj_list),
]