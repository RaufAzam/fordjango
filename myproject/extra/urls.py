from django.urls import path
from extra import views 

urlpatterns = [
    path("fof_alt/", views.fof_alt),
    path("fof_two/", views.fof_two),
    path("fof/", views.fof),
    path("foo_two/", views.foo_two),
    path("foo/", views.foo),
    path("coming_soon/", views.coming_soon),
    path("faqs/", views.faqs),
    path("gallery/", views.gallery),
    path("invoice/", views.invoice),
    path("maintenance/", views.maintenance),
    path("pricing/", views.pricing),
    path("search_results/", views.search_results),
    path("sitemap/", views.sitemap),
    path("starter/", views.starter),
    path("timeline/", views.timeline),
]