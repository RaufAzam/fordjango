from django.shortcuts import render

# Create your views here.
def dripicons(request):
    return render(request, "components/icons/dripicons.html")
def feather(request):
    return render(request, "components/icons/feather.html")
def front_awesome(request):
    return render(request, "components/icons/font-awesome.html")
def mdi(request):
    return render(request, "components/icons/mdi.html")
def simple_line(request):
    return render(request, "components/icons/simple-line.html")
def themify(request):
    return render(request, "components/icons/themify.html")
def two_tone(request):
    return render(request, "components/icons/two-tone.html")
def weather(request):
    return render(request, "components/icons/weather.html")