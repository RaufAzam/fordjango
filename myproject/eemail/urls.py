from django.urls import path
from eemail import views 

urlpatterns = [
    path("eml_compose/",views.eml_compose),
    path("eml_inbox/", views.eml_inbox),
    path("eml_read/", views.eml_read),
    path("eml_temp/", views.eml_temp),
    path("eml_temp_alert/", views.eml_temp_alert),
    path("eml_temp_billing/", views.eml_temp_billing),
    path("eml_templates_action/", views.eml_templates_action),
]