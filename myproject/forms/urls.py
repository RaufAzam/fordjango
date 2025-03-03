from django.urls import path
from forms import views 

urlpatterns = [
    path("advanced/", views.advanced),
    path("elements/", views.elements),
    path("file_uloads/", views.file_uloads),
    path("image_crop/", views.image_crop),
    path("masks/", views.masks),
    path("pickers/", views.pickers),
    path("quilljs/", views.quilljs),
    path("validation/", views.validation),
    path("wizard/", views.wizard),
    path("x_editable/", views.x_editable),
]