from django.shortcuts import render

# Create your views here.
def tkt_detail(request):
    return render(request, "apps/tickets/detail.html")
def tkt_list(request):
    return render(request, "apps/tickets/list.html")