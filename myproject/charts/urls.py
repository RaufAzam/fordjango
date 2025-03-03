from django.urls import path
from charts import views 

urlpatterns = [
    path("apex/", views.apex),
    path("c3/", views.c3),
    path("chartist/", views.chartist),
    path("chartjs/", views.chartjs),
    path("flot/", views.flot),
    path("knob/", views.knob),
    path("morris/", views.morris),
    path("peity/", views.peity),
    path("sparklines/", views.sparklines),
]