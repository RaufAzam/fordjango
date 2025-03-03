from django.urls import path
from tasks import views

urlpatterns = [
    path("tsk_details/", views.tsk_details),
    path("tsk_kanban_board/", views.tsk_kanban_board),
    path("tsk_list/", views.tsk_list),
]