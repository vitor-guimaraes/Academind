from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import date

from . models import Post

# 1. Create View
# 2. Create URL paths, linking views.py with urls.py
# 3. Create HTML page on templates folder
# 4. Include App.urls file on Project.urls file
# 5. Add app to installed apps on Project settings.py
# 6. Add BASE_DIR to settings file to pick up global templates


def index(request):
    try:
        latest_posts = Post.objects.all().order_by("-date")[:3]
        return render(request, "blog/index.html", {
            "posts": latest_posts
        })
    except:
        raise Http404()


def posts(request):
    try:
        all_posts = Post.objects.all().order_by("-date")
        return render(request, "blog/posts.html",{
            "posts": all_posts})
    except:
        raise Http404()


def detail_post(request, slug):
    try:
        # identified_post = get_object_or_404(Post, slug=slug)
        identified_post = Post.objects.get(slug=slug)
        return render(request, "blog/details.html", {
            "post": identified_post,
            "post_tags": identified_post.tags.all()
        })
    except:
        raise Http404()
    

def get_date(post):
    return post.get('date')
    # alternative syntax: return post['date']