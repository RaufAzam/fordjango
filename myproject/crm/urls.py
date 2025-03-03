from django.urls import path
from crm import views 

urlpatterns = [
    path("contacts/", views.crmcontacts),
    path("crmcustomers/", views.crmcustomers),
    path("crmdashboard/", views.crmdashboard),
    path("leads/", views.crmleads),
    path("opportunities/", views.crmopportunities),
]