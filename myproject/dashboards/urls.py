from django.urls import path
from dashboards import views 

urlpatterns = [
    path("dashboard_2/", views.dashboard_2),
    path("dashboard_3/", views.dashboard_3),
    path("dashboard_4/", views.dashboard_4),
    path("index/", views.index),
]