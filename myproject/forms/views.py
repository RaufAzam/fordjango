from django.shortcuts import render

# Create your views here.
def advanced(request):
    return render(request, "components/forms/advanced.html")
def elements(request):
    return render(request, "components/forms/elements.html")
def file_uloads(request):
    return render(request, "components/forms/file-uploads.html")
def image_crop(request):
    return render(request, "components/forms/image-crop.html")
def masks(request):
    return render(request, "components/forms/masks.html")
def pickers(request):
    return render(request, "components/forms/pickers.html")
def quilljs(request):
    return render(request, "components/forms/quilljs.html")
def validation(request):
    return render(request, "components/forms/validation.html")
def wizard(request):
    return render(request, "components/forms/wizard.html")
def x_editable(request):
    return render(request, "components/forms/x-editable.html")