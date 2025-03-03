from django.shortcuts import render

# Create your views here.
def animation(request):
    return render(request, "components/extended/animation.html")
def dragula(request):
    return render(request, "components/extended/dragula.html")
def loading_buttons(request):
    return render(request, "components/extended/loading-buttons.html")
def nestable(request):
    return render(request, "components/extended/nestable.html")
def range_slider(request):
    return render(request, "components/extended/range-slider.html")
def scrollspy(request):
    return render(request, "components/extended/scrollspy.html")
def sweet_alert(request):
    return render(request, "components/extended/sweet-alert.html")
def tour(request):
    return render(request, "components/extended/tour.html")