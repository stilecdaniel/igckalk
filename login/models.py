from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

class CustomUser(AbstractUser):
    lang = models.CharField(max_length=10, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE, verbose_name=_("Jazyk"))
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=100, verbose_name=_("Obchodné meno"))
    business_address = models.CharField(max_length=200, verbose_name=_("Adresa podnikania"))
    phone_number = models.CharField(max_length=20, verbose_name=_("Telefónne číslo"))
    ico = models.CharField(max_length=15, verbose_name=_("IČO"))
    dic = models.CharField(max_length=20, verbose_name=_("DIČ"))
    iban = models.CharField(max_length=34, verbose_name=_("IBAN"))
    rabat = models.CharField(max_length=20, verbose_name=_("Rabat"), null=True, blank=True)
    skonto = models.CharField(max_length=20, verbose_name=_("Skonto"), null=True, blank=True)


    groups = models.ManyToManyField(
        Group,
        verbose_name=_("Groups"),
        blank=True,
        related_name="customuser_set",  
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("User permissions"),
        blank=True,
        related_name="customuser_set",  
        related_query_name="user",
    )


    def __str__(self):
        return self.username
