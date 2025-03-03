from django.shortcuts import render

# Create your views here.
def ecart(request):
    return render(request, "apps/ecommerce/cart.html")
def checkout(request):
    return render(request, "apps/ecommerce/checkout.html")
def eccustomers(request):
    return render(request, "apps/ecommerce/customers.html")
def ecdashboard(request):
    return render(request, "apps/ecommerce/dashboard.html")
def orderdetail(request):
    return render(request, "apps/ecommerce/order-detail.html")
def orders(request):
    return render(request, "apps/ecommerce/orders.html")
def productdetail(request):
    return render(request, "apps/ecommerce/product-detail.html")
def productedit(request):
    return render(request, "apps/ecommerce/product-edit.html")
def products(request):
    return render(request, "apps/ecommerce/products.html")
def sellers(request):
    return render(request, "apps/ecommerce/sellers.html")