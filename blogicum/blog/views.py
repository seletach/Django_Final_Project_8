from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone
from django.http import Http404
# .order_by('-pub_date') 13 строка

#def filter_posts():
#    Post.objects.filter(
#        is_published=True,
#        category__is_published=True,
#        pub_date__lte=timezone.now())


def index(request):
    const_number_of_posts = 5
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )[:const_number_of_posts]
    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id)
    if (post.pub_date > timezone.now() or not post.is_published
            or not post.category.is_published):
        raise Http404
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)
    posts = Post.objects.filter(category=category,
                                is_published=True,
                                pub_date__lte=timezone.now())
    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, 'blog/category.html', context)
