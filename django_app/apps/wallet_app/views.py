from django.shortcuts import render
from django.views.generic.base import TemplateView, View
# Create your views here.

class IndexView(TemplateView):
    template_name = 'pages/home.html'
    page_name = 'Главная'

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        return super().get_context_data(**kwargs)