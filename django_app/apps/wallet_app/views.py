from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from apps.wallet_app.forms import TransactionForm
from apps.wallet_app.models import Wallet
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.wallet_app.models import Transaction
from django.core.paginator import Paginator
import requests
import json


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'pages/home.html'
    page_name = 'Главная'
    permission_classes = []
    
    def post(self, request):
        context = self.get_context_data()
        form = TransactionForm(self.request.POST)
        if form.is_valid():
            form.create(user=request.user)
            return redirect(reverse('home'))
        else:
            context['form'] = form
            return render(request, self.template_name, context)
    
    def get(self, request):
        context = self.get_context_data()
        transactions = Transaction.objects.all().order_by('-created_at')
        paginator = Paginator(transactions, 10)  # Show 10 transactions per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['form'] = TransactionForm()
        context['request_user'] = request.user.pk
        return render(request, self.template_name, context)


@login_required
def cancel_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.status = Transaction.Status.CANCELED
    transaction.save()
    return redirect('home')

@login_required
def approve_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction_data = {
        'subaccountID': transaction.wallet.subaccount_id,
        'recipient_address': transaction.recipient_address,
        'amount': transaction.amount,
    }
    r = requests.post('https://api.mockfly.dev/mocks/55a12083-09da-45be-b7b3-2d4dca10c622/approve', data=transaction_data)
    data = json.loads(r.text)
    if data.status == 'ok':
        transaction.status = Transaction.Status.APPROVED
        transaction.save()
    return redirect('home')