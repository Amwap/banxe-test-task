from decimal import Decimal, DecimalException
from django import forms
from apps.wallet_app.models import Transaction


class TransactionForm(forms.ModelForm):
    amount = forms.DecimalField(
        min_value=0,
        decimal_places=10,
        widget=forms.NumberInput(attrs={'step': '0.00000001'})
    )
    class Meta:
        model = Transaction
        fields = [
            'wallet',
            'recipient_address',
            'amount',
        ]
        
    def create(self, user):
        return Transaction.objects.create(
            user=user,
            wallet = self.cleaned_data['wallet'],
            recipient_address = self.cleaned_data['recipient_address'],
            amount = self.cleaned_data['amount'],
        )
        
