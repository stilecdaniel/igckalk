from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from .models import CustomUser
from django.conf import settings

class RegisterForm(UserCreationForm):
    lang = forms.ChoiceField(choices=settings.LANGUAGES, label=_("Jazyk"))
    email = forms.EmailField()
    company_name = forms.CharField(max_length=100, label=_("Obchodné meno"))
    business_address = forms.CharField(max_length=200, label=_("Adresa podnikania"))
    phone_number = forms.CharField(max_length=20, label=_("Telefónne číslo"))
    ico = forms.CharField(max_length=15, label=_("IČO"))
    dic = forms.CharField(max_length=20, label=_("DIČ"))
    iban = forms.CharField(max_length=34, label=_("IBAN"))

    class Meta:
        model = CustomUser
        fields = ["lang", "username", "first_name", "last_name", "email", "password1", "password2", "company_name", "business_address", "phone_number", "ico", "dic", "iban"]
