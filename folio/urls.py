from django.urls import path
from . import views
urlpatterns=[
    path('',views.Portfolios.as_view()),
    path('<int:pk>',views.PortfolioDetail.as_view()),
]