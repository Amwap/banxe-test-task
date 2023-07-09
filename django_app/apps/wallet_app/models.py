from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users_app.models import User
from django.utils import timezone


class Wallet(models.Model):
    address = models.CharField(_("Address"), max_length=50)
    subaccount_id = models.CharField(_("subaccountID"), max_length=50)
    network = models.CharField(_("Network"), max_length=50)
    currency = models.CharField(_("Currency"), max_length=50)
    
    def __str__(self) -> str:
        return f'{self.network}, {self.currency}'
    
    class Meta:
        verbose_name = _('Wallet')
        verbose_name_plural = _('Wallet list')


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, verbose_name=_("Service wallet"), on_delete=models.CASCADE)
    recipient_address = models.CharField(_("Recipient address"), max_length=50)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    
    def __str__(self) -> str:
        return f'{self.wallet.network} {self.wallet.currency}'
    
    class Meta:
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transaction list')
