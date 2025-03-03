from django.shortcuts import render

# Create your views here.
def tsk_details(request):
    return render(request, "apps/task/details.html")
def tsk_kanban_board(request):
    return render(request, "apps/task/kanban-board.html")
def tsk_list(request):
    return render(request, "apps/task/list.html")