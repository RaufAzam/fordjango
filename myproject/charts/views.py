from django.shortcuts import render

# Create your views here.
def apex(request):
    return render(request, "components/charts/apex.html")
def c3(request):
    return render(request, "components/charts/c3.html")
def chartist(request):
    return render(request, "components/charts/chartist.html")
def chartjs(request):
    return render(request, "components/charts/chartjs.html")
def flot(request):
    return render(request, "components/charts/flot.html")
def knob(request):
    return render(request, "components/charts/knob.html")
def morris(request):
    return render(request, "components/charts/morris.html")
def peity(request):
    return render(request, "components/charts/peity.html")
def sparklines(request):
    return render(request, "components/charts/sparklines.html")