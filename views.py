from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

import makEasy


def index(request):
    return render(request, 'makeasy/index.html')

@ensure_csrf_cookie
def item(request):
    return render(request, 'makeasy/item.html')
