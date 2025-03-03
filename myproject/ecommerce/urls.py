from django.urls import path
from ecommerce import views 

urlpatterns = [
    path("ecart/", views.ecart),
    path("checkout/", views.checkout),
    path("customers/", views.eccustomers),
    path("dashboard/", views.ecdashboard),
    path("orderdetail/", views.orderdetail),
    path("orders/", views.orders),
    path("productdetail/", views.productdetail),
    path("productedit/", views.productedit),
    path("products/", views.products),
    path("sellers/", views.sellers),
]