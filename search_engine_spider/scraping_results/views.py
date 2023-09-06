from django.core.paginator import Paginator, EmptyPage, Page
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from scraping_results.forms import SearchForm
from scraping_results.models import ScrapingResult


def search_page(request):
    form = SearchForm()
    return render(request, 'scraping_results/search_form.html', {'form': form})


SEARCH_RESULTS_PAGE_SIZE = 10


def search_results(request):
    is_ajax = request.GET.get('is_ajax', False)
    query = request.GET.get('query')
    form = SearchForm()
    form.query = query
    results = ScrapingResult.objects.filter(content__icontains=query) if query else []

    paginator = Paginator(results, SEARCH_RESULTS_PAGE_SIZE)
    page_number = int(request.GET.get('page', 1))

    page_obj = None
    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = Page([], page_obj, paginator)

    if not is_ajax:
        context = {
            'search_results': page_obj,
            'form': form,
        }
        return render(request, 'scraping_results/search_results.html', context)
    else:
        content = ''
        for result in page_obj:
            content += render_to_string('scraping_results/search_result_item.html', {'result': result}, request=request)
        return JsonResponse({
            "content": content,
            "end_pagination": page_number >= paginator.num_pages,
        })
