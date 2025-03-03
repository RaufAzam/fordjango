from django.urls import path
from baseui import views 

urlpatterns = [
    path("compbaseavatars/", views.compbaseavatars),
    path("bsbuttons/", views.bsbuttons),
    path("compcards/", views.compcards),
    path("carousel/", views.carousel),
    path("dropdowns/", views.dropdowns),
    path("general/", views.general),
    path("grid/", views.grid),
    path("images/", views.images),
    path("list_group/", views.list_group),
    path("modals/", views.modals),
    path("notifications/", views.notifications),
    path("offcanvas/", views.offcanvas),
    path("portlets/", views.portlets),
    path("ribbons/", views.ribbons),
    path("spinners/", views.spinners),
    path("tabs_accordions/", views.tabs_accordions),
    path("tooltips_popovers/", views.tooltips_popovers),
    path("typography/", views.typography),
    path("video/", views.video),
    path("progress/", views.progress),

]