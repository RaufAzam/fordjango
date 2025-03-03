from django.shortcuts import render

# Create your views here.
def compbaseavatars(request):
    return render(request, "components/base-ui/avatars.html")
def bsbuttons(request):
    return render(request, "components/base-ui/buttons.html")
def compcards(request):
    return render(request, "components/base-ui/cards.html")
def carousel(request):
    return render(request, "components/base-ui/carousel.html")
def dropdowns(request):
    return render(request, "components/base-ui/dropdowns.html")
def general(request):
    return render(request, "components/base-ui/general.html")
def grid(request):
    return render(request, "components/base-ui/grid.html")
def images(request):
    return render(request, "components/base-ui/images.html")
def list_group(request):
    return render(request, "components/base-ui/list-group.html")
def modals(request):
    return render(request, "components/base-ui/modals.html")
def notifications(request):
    return render(request, "components/base-ui/notifications.html")
def offcanvas(request):
    return render(request, "components/base-ui/offcanvas.html")
def portlets(request):
    return render(request, "components/base-ui/portlets.html")
def progress(request):
    return render(request, "components/base-ui/progress.html")
def ribbons(request):
    return render(request, "components/base-ui/ribbons.html")
def spinners(request):
    return render(request, "components/base-ui/spinners.html")
def tabs_accordions(request):
    return render(request, "components/base-ui/tabs-accordions.html")
def tooltips_popovers(request):
    return render(request, "components/base-ui/tooltips-popovers.html")
def typography(request):
    return render(request, "components/base-ui/typography.html")
def video(request):
    return render(request, "components/base-ui/video.html")