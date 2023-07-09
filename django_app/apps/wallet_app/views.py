from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from apps.wallet_app.forms import TransactionForm
from apps.wallet_app.models import Wallet
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'pages/home.html'
    page_name = 'Главная'
    permission_classes = []
    
    def post(self, request):
        context = self.get_context_data()
        form = TransactionForm(self.request.POST)
        if form.is_valid():
            form.create()
            return redirect(reverse('home'))
        else:
            context['form'] = form
            return render(request, self.template_name, context)
    
    def get(self, request):
        context = self.get_context_data()
        context['form'] = TransactionForm()
        return render(request, self.template_name, context)