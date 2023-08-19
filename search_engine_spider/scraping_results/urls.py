from django.urls import path
from scraping_results import views


urlpatterns = [
    path('', views.search_page, name="home_page"),
]
