"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/",include("myapp.urls")),
    path("account/", include("account.urls")),
    path("calendr/", include("calendr.urls")),
    path("chat/", include("chat.urls")),
    path("ecommerce/", include("ecommerce.urls")),
    path("crm/", include("crm.urls")),
    path("email/", include("eemail.urls")),
    path("projects/", include("projects.urls")),
    path("tasks/", include("tasks.urls")),
    path("contacts/", include("contacts.urls")),
    path("tickets/", include("tickets.urls")),
    path("auth/", include("authpage.urls")),
    path("baseui/", include("baseui.urls")),
    path("extra/", include("extra.urls")),
    path("layouts/", include("layouts.urls")),
    path("extended/", include("extended.urls")),
    path("icons/", include("icons.urls")),
    path("forms/", include("forms.urls")),
    path("tables/", include("tables.urls")),
    path("charts/", include("charts.urls")),
    path("maps/", include("maps.urls")),
    path("dashboards/", include("dashboards.urls")),
]
