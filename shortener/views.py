from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render

from .forms import UrlForm
from .models import Url
from .utils import get_unique_slug 


def index(request):
    if not request.method == "POST":
        form = UrlForm()
        return render(request,
            "shortener/index.html", 
            {
                "form": form,
            }
        )
    form = UrlForm(request.POST)
    if not form.is_valid():
        return render(
            request,
            "shortener/index.html", 
            {
                "form": form,
            }
        )
    short_url = form.save(commit=False)
    short_url.slug = get_unique_slug()
    short_url.save()

    return render(request, 
        "shortener/index.html", 
        {
            "form": form,
            "short_url": f"{settings.SITE_URL}go/{short_url.slug}"
        }
    )

def url_detail(request, slug):
    url_obj = get_object_or_404(Url, slug=slug)
    url_obj.nums_of_visits += 1
    url_obj.save()
    return redirect(url_obj.full_url)

