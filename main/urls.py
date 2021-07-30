from django.urls import path

# Import custom views
from . import views

# Paths array
urlpatterns = [
    path("", views.home, name="Homepage"),
    path("clients", views.clients, name="clients-list"),
    path("clients/<int:id>", views.client, name="client-info"),
    # path("clients/<int:id>/update", views.updateClient, name="client-update"),
    path("clients/<int:id>/delete", views.deleteClient, name="client-delete"),
    path("clients/create", views.createClient, name="client-create"),
    path("banks", views.banks, name="banks-list"),
    path("banks/<int:id>", views.bank, name="bank-info"),
    path("banks/create", views.createBank, name="bank-create"),
    path("credits", views.credits, name="credits-list"),
    path("credits/<int:id>", views.credit, name="credit-info"),
    path("credits/create", views.createCredit, name="credit-create"),
]