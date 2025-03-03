from django.shortcuts import render

# Create your views here.
def dashboard_2(request):
    return render(request, "dashboard/dashboard-2.html")
def dashboard_3(request):
    return render(request, "dashboard/dashboard-3.html")
def dashboard_4(request):
    return render(request, "dashboard/dashboard-4.html")
def index(request):
    return render(request, "dashboard/index.html")