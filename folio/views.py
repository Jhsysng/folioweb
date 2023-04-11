from django.shortcuts import render
from .models import Portfolio, LangTag, TechTag
from django.views.generic import ListView,DetailView,TemplateView
from django.db.models import Q


class Portfolios(ListView):
    model = Portfolio
    ordering = '-pk'
    template_name = 'folio/portfolios.html'


class PortfolioDetail(DetailView):
    model = Portfolio
    template_name = 'folio/portfolio.html'


class SearchView(ListView):
    template_name = 'folio/search.html'

    def get_queryset(self):
        query = self.kwargs['q']
        lang_tags = LangTag.objects.filter(Q(name__icontains=query))
        tech_tags = TechTag.objects.filter(Q(name__icontains=query))
        portfolios = Portfolio.objects.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()

        return {
            'lang_tags':lang_tags,
            'tech_tags':tech_tags,
            'portfolios':portfolios,
        }

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        query = self.kwargs['q']
        context['lang_tags'] = self.get_queryset()['lang_tags']
        context['tech_tags'] = self.get_queryset()['tech_tags']
        context['portfolios'] = self.get_queryset()['portfolios']
        return context