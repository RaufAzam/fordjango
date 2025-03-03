from django.shortcuts import render

# Create your views here.
def fof_alt(request):
    return render(request, "extra/404-alt.html")
def fof_two(request):
    return render(request, "extra/404-two.html")
def fof(request):
    return render(request, "extra/404.html")
def foo_two(request):
    return render(request, "extra/500-two.html")
def foo(request):
    return render(request, "extra/500.html")
def coming_soon(request):
    return render(request, "extra/coming-soon.html")
def faqs(request):
    return render(request, "extra/faqs.html")
def gallery(request):
    return render(request, "extra/gallery.html")
def invoice(request):
    return render(request, "extra/invoice.html")
def maintenance(request):
    return render(request, "extra/maintenance.html")
def pricing(request):
    return render(request, "extra/pricing.html")
def search_results(request):
    return render(request, "extra/search-results.html")
def sitemap(request):
    return render(request, "extra/sitemap.html")
def starter(request):
    return render(request, "extra/starter.html")
def timeline(request):
    return render(request, "extra/timeline.html")