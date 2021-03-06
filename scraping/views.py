from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm
# Create your views here.


def home_views(request):
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language

        qs = Vacancy.objects.filter(**_filter)
    return render(request, 'scraping/home.html', context={'object_list':qs, 'form':FindForm})


