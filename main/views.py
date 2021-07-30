from django.shortcuts import render
from django.http import HttpResponse

# Import the custom models
from .models import Bank, Client, Credit

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

# CLIENTS
def clients(response):
    data = Client.objects.all

    return render(response, "main/clients/list.html", { "clients": data })

def client(response, id):
    data = Client.objects.get(id=id)

    return render(response, "main/clients/info.html", { "client": data })

# BANKS
def banks(response):
    data = Bank.objects.all

    return render(response, "main/banks/list.html", { "banks": data })

def bank(response, id):
    data = Bank.objects.get(id=id)

    return render(response, "main/banks/info.html", { "bank": data })

# CREDITS
def credits(response):
    data = Credit.objects.all

    return render(response, "main/credits/list.html", { "credits": data })

def credit(response, id):
    data = Credit.objects.get(id=id)

    return render(response, "main/credits/info.html", { "credit": data })