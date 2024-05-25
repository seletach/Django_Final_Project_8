from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone


query_set_post = Post.objects


def filter_posts(request):
    return request.filter(is_published=True,
                          category__is_published=True,
                          pub_date__lte=timezone.now())


def index(request):
    CONST_NUMBER_OF_POSTS: int = 5
    post_list = filter_posts(query_set_post)[:CONST_NUMBER_OF_POSTS]
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(filter_posts(query_set_post), id=id)
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category_list = get_object_or_404(Category,
                                      slug=category_slug,
                                      is_published=True)
    posts = Post.objects.filter(category=category_list,
                                is_published=True,
                                pub_date__lte=timezone.now())
    context = {
        'category': category_list,
        'post_list': posts
    }
    return render(request, 'blog/category.html', context)
