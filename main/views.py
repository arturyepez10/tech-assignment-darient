from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Import the custom models
from .models import Bank, Client, Credit

# Import the custom Forms
from .forms import CreateNewBank, CreateNewCredit, CreateNewClient

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

def createClient(response):
    if response.method == "POST":
        form = CreateNewClient(response.POST)
        if form.is_valid():
            data = form.cleaned_data
            cl = Client(
                firstName=data["firstName"],
                lastName=data["lastName"],
                birthDate=data["birthDate"],
                age=data["age"],
                nationality=data["nationality"],
                address=data["address"],
                email=data["email"],
                phone=data["phone"]
            )
            cl.save()
            return HttpResponseRedirect('/clients')
    else:
        form = CreateNewClient()
    
    variables = {
        "form": form,
        "name": "Create Client",
        "actionName": "/clients/create",
        "buttonName": "Create New Client"
    }

    return render(response, "main/create.html", variables) 

# BANKS
def banks(response):
    data = Bank.objects.all

    return render(response, "main/banks/list.html", { "banks": data })

def bank(response, id):
    data = Bank.objects.get(id=id)

    return render(response, "main/banks/info.html", { "bank": data })

def createBank(response):
    if response.method == "POST":
        form = CreateNewBank(response.POST)
        if form.is_valid():
            data = form.cleaned_data
            b = Bank(name=data["name"], address=data["address"], bankType=data["bankType"])
            b.save()
            return HttpResponseRedirect('/banks')
    else: 
        form = CreateNewBank()

    variables = {
        "form": form,
        "name": "Create Bank",
        "actionName": "/banks/create",
        "buttonName": "Create New Bank"
    }

    return render(response, "main/create.html", variables)

# CREDITS
def credits(response):
    data = Credit.objects.all

    return render(response, "main/credits/list.html", { "credits": data })

def credit(response, id):
    data = Credit.objects.get(id=id)

    return render(response, "main/credits/info.html", { "credit": data })

def createCredit(response):
    if response.method == "POST":
        form = CreateNewCredit(response.POST)
        if form.is_valid():
            data = form.cleaned_data
            c = Credit(
                clientOwner=data["clientOwner"],
                bankOwner=data["bankOwner"],
                description=data["description"],
                minPayment=data["minPayment"],
                maxPayment=data["maxPayment"],
                termsOfCredits=data["termsOfCredits"],
                creditType=data["creditType"]
            )
            c.save()
            return HttpResponseRedirect('/credits')
    else:
        form = CreateNewCredit()

    variables = {
        "form": form,
        "name": "Create Bank",
        "actionName": "/credits/create",
        "buttonName": "Assign New Credit"
    }
    
    return render(response, "main/create.html", variables)