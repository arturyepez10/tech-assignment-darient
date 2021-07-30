from django import forms
from django.core.validators import EmailValidator

# Import the models necessary
from .models import Bank, Client

# Constants
BANK_TYPES= (
    ('P', 'Private'),
    ('G', 'BANK_TYPES')
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


# BANK FORM
class CreateNewClient(forms.Form):
    firstName = forms.CharField(max_length=40, label="First Name")
    lastName = forms.CharField(max_length=40, label="Last Name")
    birthDate = forms.DateField(label="Birth Date", help_text="Format should be YYYY-MM-DD")
    age = forms.IntegerField(min_value=1, max_value=99, required=False)
    nationality = forms.CharField(max_length=50, required=False)
    address = forms.CharField(max_length=200, required=False)
    email = forms.EmailField(validators=[EmailValidator(allowlist=["prueba.com"])])
    phone = forms.CharField(max_length=20, required=False)
    clienType = forms.ChoiceField(choices=CLIENT_TYPES, label="Client Type")


class CreateNewBank(forms.Form):
    name = forms.CharField(max_length=80, label="Name")
    address = forms.CharField(max_length=200, required=False)
    bankType = forms.ChoiceField(choices=BANK_TYPES, label="Type of Bank")

class CreateNewCredit(forms.Form):
    clientOwner = forms.ModelChoiceField(queryset=Client.objects.all(), label="Client")
    bankOwner = forms.ModelChoiceField(queryset=Bank.objects.all(), label="Bank")
    description = forms.CharField(max_length=200, label="Description")
    minPayment = forms.DecimalField(max_digits=12, decimal_places=2, label="Min. Payment")
    maxPayment = forms.DecimalField(max_digits=12, decimal_places=2, label="Max. Payment")
    termsOfCredits = forms.IntegerField(label="Terms of Loan (months)")
    creditType = forms.ChoiceField(choices=CREDIT_TYPES, label="Type of Credit")