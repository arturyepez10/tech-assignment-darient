from django.urls import path

# Import custom views
from . import views

# Paths array
urlpatterns = [
    path("", views.home, name="Homepage"),
    path("clients", views.clients, name="clients-list"),
    path("clients/<int:id>", views.client, name="client-info"),
    path("banks", views.banks, name="banks-list"),
    path("banks/<int:id>", views.bank, name="bank-info"),
    path("credits", views.credits, name="credits-list"),
    path("credits/<int:id>", views.credit, name="credit-info"),
]