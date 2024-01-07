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

class BaseChimney(models.Model):
    length = models.DecimalField(max_digits=10, decimal_places=1, verbose_name=_("Dĺžka komína (m)"), help_text=_("Povoľujeme zadať číslo s jednou desatinou"))


    class Meta:
        abstract = True

class PPsT120(BaseChimney):
    internal_diameter = models.IntegerField(choices=[(60, '60'), (80, '80'), (100, '100'), (110, '110'), (125, '125'), (160, '160'), (200, '200')], verbose_name=_("Vnútorný priemer (mm)"), default = (60, '60'))

class PPsALT120(BaseChimney):
    internal_external_diameter = models.CharField(max_length=10, choices=[('60/100', '60/100'), ('80/125', '80/125'), ('100/150', '100/150'), ('110/160', '110/160'), ('125/180', '125/180')],verbose_name=_("Vnútorný/Vonkajší priemer (mm)"), default = ('60/100', '60/100'))
    roof_pass = models.CharField(max_length=20, choices=[('bez prechodu', 'bez prechodu'), ('plochá prechodka', 'plochá prechodka'), ('šikmá prechodka', 'šikmá prechodka')], verbose_name=_("Prechod strechou"), default = ('bez prechodu', 'bez prechodu'))

class ALT200(BaseChimney):
    internal_diameter = models.IntegerField(choices=[(60, '60'), (80, '80'), (100, '100'), (125, '125')], verbose_name=_("Vnútorný priemer (mm)"), default = (60, '60'))

class ALALT200(BaseChimney):
    internal_external_diameter = models.CharField(max_length=10, choices=[('60/100', '60/100'), ('80/125', '80/125'), ('100/150', '100/150'), ('125/180', '125/180')],verbose_name=_("Vnútorný/Vonkajší priemer (mm)"), default = ('60/100', '60/100'))
    roof_pass = models.CharField(max_length=20, choices=[('bez prechodu', 'bez prechodu'), ('plochá prechodka', 'plochá prechodka'), ('šikmá prechodka', 'šikmá prechodka')], verbose_name=_("Prechod strechou"), default = ('bez prechodu', 'bez prechodu'))

class ALALT300(BaseChimney):
    chimney_design = models.CharField(max_length=20, choices=[("jednovrstvový systém","jednovrstvový systém"),("koncentrický systém","koncentrický systém"),("izolovaný systém","izolovaný systém")], default = ("jednovrstvový systém","jednovrstvový systém"), verbose_name=_("Prevedenie komínového systému"))
    internal_diameter = models.IntegerField(choices=[(80, '80'), (100, '100'), (125, '125')], verbose_name=_("Vnútorný priemer (mm)"), default = (80, '80'))
    internal_external_diameter = models.CharField(max_length=10, choices=[('80/125', '80/125'), ('100/150', '100/150'), ('125/180', '125/180')],verbose_name=_("Vnútorný/Vonkajší priemer (mm)"), default = ('80/125', '80/125'))