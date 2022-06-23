from django.shortcuts import redirect, render
from .models import *
# Create your views here.


def index(request):
    data = {
        'url': ""
    }
    return render(request, 'index.html', data)


def short(request):
    url = request.POST['url']

    try:
        my_url = user_url.objects.get(url=url)
    except:
        new_obj = user_url()
        new_obj.url = url
        new_obj.save()

    my_url = user_url.objects.get(url=url)
    data = {
        'url': f"http://127.0.0.1:8000/{my_url.id}"
    }
    return render(request, 'answer.html', data)


def urlshort(request, id):
    my_url = user_url.objects.get(id=id).url
    return redirect(f"http://{my_url}")
