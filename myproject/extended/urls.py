from django.urls import path
from extended import views 

urlpatterns =[
    path("animation/", views.animation),
    path("dragula/", views.dragula),
    path("loading_buttons/", views.loading_buttons),
    path("nestable/", views.nestable),
    path("range_slider/", views.range_slider),
    path("scrollspy/", views.scrollspy),
    path("sweet_alert/", views.sweet_alert),
    path("tour/", views.tour),
]