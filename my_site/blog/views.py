from django.shortcuts import render
from django.http import HttpResponse, Http404


# 1. Create View
# 2. Create URL paths, linking views.py with urls.py
# 3. Create HTML page on templates folder
# 4. Include App.urls file on Project.urls file
# 5. Add app to installed apps on Project settings.py
# 6. Add BASE_DIR to settings file to pick up global templates

def index(request):
    # try:
        return render(request, "blog/index.html")
    # except:
    #     raise Http404()


def posts(request):
    try:
        return render(request, "blog/posts.html")
    except:
        raise Http404()


def detail_post(request, slug):
    try:
        return render(request, "blog/details.html")
    except:
        raise Http404()