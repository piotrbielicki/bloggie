from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


# def post_list(request):
#     posts = Post.published.all()
#     return render(request,
#                   'bloggie/post/list.html',
#                   {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'bloggie/post/detail.html',
                  {'post': post})


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posty na każdej stronie
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #jeśli zmienna page nie jest liczbą całkowitą,
        #pobierana jest pierwsza strona wyników.
        posts = paginator.page(1)
    except EmptyPage:
        # jeśli zmienna ma wartość większą niż numer ostatniej
        # strony, pobierana jest ostatnia strona wyników.
        posts = paginator.page(paginator.num_pages)


    return render(request, 'blog/post/list.html', {'page': page,
                                               'posts': posts})

