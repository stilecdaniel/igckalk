from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _
from .models import *
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

class PPsT120Form(forms.ModelForm):
    class Meta:
        model = PPsT120
        fields = ["length", "internal_diameter"]

class PPsALT120Form(forms.ModelForm):
    class Meta:
        model = PPsALT120
        fields = ["length", "internal_external_diameter", "roof_pass"]

class ALT200Form(forms.ModelForm):
    class Meta:
        model = ALT200
        fields = ["length", "internal_diameter"]

class ALALT200Form(forms.ModelForm):
    class Meta:
        model = ALALT200
        fields = ["length", "internal_external_diameter", "roof_pass"]

class ALALT300Form(forms.ModelForm):
    class Meta:
        model = ALALT300
        fields = ['length', 'chimney_design']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Dynamically adjust fields based on the selected chimney_design
        chimney_design = self.instance.chimney_design if self.instance.pk else None

        # Remove existing fields
        for field_name in list(self.fields.keys()):
            if field_name not in self.Meta.fields:
                del self.fields[field_name]

        # Add fields based on the selected chimney_design
        if chimney_design == "jednovrstvový systém":
            self.fields['internal_diameter'] = forms.IntegerField(
                choices=[(80, '80'), (100, '100'), (125, '125')],
                label=_("Vnútorný priemer (mm)"),
            )
        elif chimney_design == "koncentrický systém":
            self.fields['internal_external_diameter'] = forms.ChoiceField(
                choices=[('60/100', '60/100'), ('80/125', '80/125'), ('100/150', '100/150')],
                label=_("Vnútorný/Vonkajší priemer (mm)"),
            )
        elif chimney_design == "izolovaný systém":
            self.fields['internal_external_diameter'] = forms.ChoiceField(
                choices=[('80/125', '80/125'), ('100/150', '100/150'), ('125/180', '125/180')],
                label=_("Vnútorný/Vonkajší priemer (mm)"),
            )