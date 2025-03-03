from django.urls import path
from layouts import views 

urlpatterns = [
    path("detached/", views.detached),
    path("horizontal/", views.horizontal),
    path("preloader_layouts/", views.preloader_layouts),
    path("two_column_layouts/", views.two_column_layouts),
    path("two_tone_icons_layouts/", views.two_tone_icons_layouts),

]