from django.shortcuts import render
# Create your views here.
def crmcontacts(request):
    return render(request, "apps/crm/contacts.html")
def crmcustomers(request):
    return render(request, "apps/crm/customers.html")
def crmdashboard(request):
    return render(request, "apps/crm/dashboard.html")
def crmleads(request):
    return render(request, "apps/crm/leads.html")
def crmopportunities(request):
    return render(request, "apps/crm/opportunities.html")
