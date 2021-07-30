from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator

# Constants
BANK_TYPES= (
    ('P', 'Private'),
    ('G', 'Gobernment')
)

CLIENT_TYPES = (
    ('N', 'Natural'),
    ('L', 'Legal')
)

CREDIT_TYPES = (
    ('A', 'Auto'),
    ('M', 'Mortgage'),
    ('C', 'Commercial')
)

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=200, null=True)
    bankType = models.CharField(max_length=1, choices=BANK_TYPES)

    def __str__(self):
        return self.name

class Client(models.Model):
    firstName = models.CharField(max_length=80)
    lastName = models.CharField(max_length=80)
    birthDate = models.DateField(auto_now=False, auto_now_add=False)
    age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)], null=True)
    nationality = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=80, validators=[ EmailValidator(allowlist=["prueba.com"])])
    phone = models.CharField(max_length=20, null=True)
    clientType = models.CharField(max_length=1, choices=CLIENT_TYPES)

    def __str__(self):
        return "%s %s" % (self.firstName, self.lastName)

class Credit(models.Model):
    clientOwner = models.ForeignKey(Client, on_delete=models.CASCADE)
    bankOwner = models.ForeignKey(Bank, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    minPayment = models.DecimalField(max_digits=12, decimal_places=2)
    maxPayment = models.DecimalField(max_digits=12, decimal_places=2)
    termsOfCredits = models.PositiveIntegerField()
    registerDate = models.DateTimeField(auto_now_add=True)
    creditType = models.CharField(max_length=1, choices=CREDIT_TYPES)

    def __str__(self):
        return "%s - %s | %s" % (self.clientOwner, self.bankOwner, self.description) 