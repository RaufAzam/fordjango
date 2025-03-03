from django.urls import path
from tables import views 

urlpatterns = [
    path("basic/", views.basic),
    path("bootstrap/", views.bootstrap),
    path("editable/", views.editable),
    path("footables/", views.footables),
    path("jsgrid/", views.jsgrid),
    path("responsive/", views.responsive),
    path("tablesaw/", views.tablesaw),
    path("datatables/", views.datatables),
]