from django.shortcuts import render

# Create your views here.
def basic(request):
    return render(request, "components/tables/basic.html")
def bootstrap(request):
    return render(request, "components/tables/bootstrap.html")
def editable(request):
    return render(request, "components/tables/editable.html")
def footables(request):
    return render(request, "components/tables/footables.html")
def jsgrid(request):
    return render(request, "components/tables/jsgrid.html")
def responsive(request):
    return render(request, "components/tables/responsive.html")
def tablesaw(request):
    return render(request, "components/tables/tablesaw.html")
def datatables(request):
    return render(request, "components/tables/datatables.html")