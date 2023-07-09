from django.contrib import admin
from apps.wallet_app.models import Wallet, Transaction


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    search_fields = ('address', 'subaccount_id', 'network', 'currency')
    list_display = ('id', 'address', 'subaccount_id', 'network', 'currency')
    list_editable = ('address', 'subaccount_id', 'network', 'currency')
    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ('wallet', 'recipient_address', 'amount')
    list_display = ('id', 'wallet', 'recipient_address', 'amount')
    list_editable = ('wallet', 'recipient_address', 'amount')