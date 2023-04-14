from . import views
from django.urls import path
urlpatterns=[
    path('',views.Portfolios.as_view()),
    path('<int:pk>',views.PortfolioDetail.as_view()),
    path('search/<str:q>/', views.SearchView.as_view()),
    path('search/',views.SearchBaseView.as_view()),
    path('techinfo/', views.TechList.as_view()),
]