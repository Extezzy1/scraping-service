from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'sam lox'
    _context = {'date':date, 'name':name}
    return render(request, './base.html', context=_context)