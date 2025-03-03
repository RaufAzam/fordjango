from django.shortcuts import render

# Create your views here.
def contactlist(request):
    return render(request, "apps/contacts/list.html")
def profilecontact(request):
    return render(request, "apps/contacts/profile.html")
def crmcontacts(request):
    return render(request, "apps/crm/contacts.html")
