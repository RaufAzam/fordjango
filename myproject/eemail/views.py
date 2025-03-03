from django.shortcuts import render

# Create your views here.
def eml_compose(request):
    return render(request, "apps/email/compose.html")
def eml_inbox(request):
    return render(request, "apps/email/inbox.html")
def eml_read(request):
    return render(request, "apps/email/read.html")
def eml_templates_action(request):
    return render(request, "apps/email/templates-action.html")
def eml_temp_alert(request):
    return render(request, "apps/email/templates-alert.html")
def eml_temp_billing(request):
    return render(request, "apps/email/templates-billing.html")
def eml_temp(request):
    return render(request, "apps/email/templates.html")