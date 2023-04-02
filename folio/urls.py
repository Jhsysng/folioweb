from . import views
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
urlpatterns=[
    path('',views.Portfolios.as_view()),
    path('<int:pk>',views.PortfolioDetail.as_view()),
]