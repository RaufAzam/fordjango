from django.shortcuts import render

# Create your views here.
def proj_create(request):
    return render(request, "apps/project/create.html")
def proj_detail(request):
    return render(request, "apps/project/detail.html")
def proj_list(request):
    return render(request, "apps/project/list.html")
