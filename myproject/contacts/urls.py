from django.urls import path
from contacts import views 

urlpatterns = [
    path("list/", views.contactlist),
    path("profile/", views.profilecontact),
    path("contacts/", views.crmcontacts),
]