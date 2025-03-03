from django.urls import path
from tickets import views 

urlpatterns = [
    path("tkt_detail/", views.tkt_detail),
    path("tkt_list/", views.tkt_list),
]