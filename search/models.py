from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class Seller(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Vor- und Nachname")
    matriculation_number = models.CharField(max_length=8, validators=[MinLengthValidator(8)],
                                            verbose_name="Matrikelnummer", unique=True)
    email = models.EmailField(verbose_name="E-Mail", unique=True)

    def __str__(self):
        return f"{self.full_name} - {self.matriculation_number}"


class Offer(models.Model):
    isbn = models.CharField(max_length=13, verbose_name="ISBN")
    wish_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Wunschpreis")
    # seller_id = models.ForeignKey() # todo: add seller_id
    member_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="FV-Mitglied")
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Erstellt am")
    modified = models.DateTimeField(auto_now=True, verbose_name="Zuletzt geändert am")
    marked = models.BooleanField(default=True, verbose_name="Markiert")
    location = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return f"{self.pk}"


class Transaction(models.Model):
    value = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Betrag")
    seller_id = models.ForeignKey("Seller", on_delete=models.PROTECT, verbose_name="Verkäufer:in")
    member_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="FV-Mitglied")
    offer_id = models.ForeignKey('Offer', on_delete=models.PROTECT) # todo: nullable
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Erstellt am")

    def save(self, *args, **kwargs):
        if self.pk is not None:  # Check if the instance already exists
            raise ValidationError("Transactions cannot be modified once created.")
        super().save(*args, **kwargs)

    def __str__(self):
        out = ""
        if self.value < 0:
            out += f"AUS: {self.value} ID:{self.offer_id}"
        else:
            out += f"EIN: {self.value} ID:{self.offer_id}"

        return out
