from django.shortcuts import render
from .models import Portfolio
from django.views.generic import ListView,DetailView
class Portfolios(ListView):
    model=Portfolio
    ordering='-pk'
    paginate_by = 5
    template_name = 'folio/portfolios.html'

    def get_context(self,**kwargs):
        context =super(Portfolios,self).get_context()
        context['no_category_post_count']=Portfolio.objects.filter(category=None).count()
        return context

class PortfolioDetail(DetailView):
    model=Portfolio
    template_name = 'folio/portfolio.html'