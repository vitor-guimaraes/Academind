from django.shortcuts import render
from django.http import HttpResponse, Http404


# 1. Create View
# 2. Create URL paths, linking views.py with urls.py
# 3. Link App URL with Project URL
# 4. Create HTML page on templates folder
# 5. Add app pto installed apps on settings.py


def index(request):
    # try:
    #     return render(request, "blog/index.html")
    # except:
    #     raise Http404()
    return render(request, "blog/index.html")




