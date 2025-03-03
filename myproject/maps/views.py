from django.shortcuts import render

# Create your views here.
def google(request):
    return render(request, "components/maps/google.html")
def mapael(request):
    return render(request, "components/maps/mapael.html")
def vector(request):
    return render(request, "components/maps/vector.html")