from django.shortcuts import render

# Create your views here.
def detached(request):
    return render(request, "layouts/detached.html")
def horizontal(request):
    return render(request, "layouts/horizontal.html")
def preloader_layouts(request):
    return render(request, "layouts/preloader-layouts.html")
def two_column_layouts(request):
    return render(request, "layouts/two-column-layouts.html")
def two_tone_icons_layouts(request):
    return render(request, "layouts/two-tone-icons-layouts.html")