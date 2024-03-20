from django.shortcuts import render
from django.http import Http404


def index(request):
    template_name = 'blog/index.html'
    return render(request, template_name)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    try:
        return render(request, template_name)
    except IndexError:
        raise Http404


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    return render(request, template_name, {'category_slug': category_slug})
