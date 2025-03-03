from django.shortcuts import render

# Create your views here.
def calendar(request):
    return render(request, "apps/calendar/calendar.html")
def newc(request):
    return render(request, "apps/calendar/newc.html")