from django.shortcuts import render

from scraping_results.forms import SearchForm


def search_page(request):
    form = SearchForm()
    return render(request, 'scraping_results/search_form.html', {'form': form})
