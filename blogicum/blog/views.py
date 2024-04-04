from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
    )
    context = {
        'post_list': post_list,
    }
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        id=id)
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)
    posts = Post.objects.filter(category=category, is_published=True)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, template_name, context)
