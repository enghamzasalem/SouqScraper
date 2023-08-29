from django.urls import path
from scraping_results import views


urlpatterns = [
    path('', views.search_page, name="home_page"),
    path('search_results', views.search_results, name='search_results'),
]
