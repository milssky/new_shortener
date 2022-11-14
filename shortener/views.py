from django.shortcuts import get_object_or_404, redirect, render

from .forms import UrlForm
from .models import Url
from .utils import get_unique_slug 


def index(request):
    form = UrlForm()
    urls = Url.objects.all()
    return render(request, "shortener/index.html", {
        'form': form,
        'urls': urls,
        })

def url_detail(request, slug):
    url = get_object_or_404(Url, slug=slug)
    


def process(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.nums_of_visits += 1
            url.slug = get_unique_slug()
            url.save()
    return redirect("shortener:index")

