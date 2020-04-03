from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
from .models import Post

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'bloggie/post/list.html'


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


# def post_list(request):
#     posts = Post.published.all()
#     return render(request,
#                   'bloggie/post/list.html',
#                   {'posts': posts})


# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3) # 3 posty na każdej stronie
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         #jeśli zmienna page nie jest liczbą całkowitą,
#         #pobierana jest pierwsza strona wyników.
#         posts = paginator.page(1)
#     except EmptyPage:
#         # jeśli zmienna ma wartość większą niż numer ostatniej
#         # strony, pobierana jest ostatnia strona wyników.
#         posts = paginator.page(paginator.num_pages)
#
#
#     return render(request, 'bloggie/post/list.html', {'page': page,
#                                                'posts': posts})

def post_share(request, post_id):
    #Pobranie posta na podstawie jego identyfikatora.
    post = get_object_or_404(Post, id=post_id, status='published')

    if request.method == 'POST':
        #formularz został wysłany.
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #weryfikacja pól formularza zakończyła się powodzeniem...
            cd = form.cleaned_data
            #...więc można wysłać wiadomość e-mail
        else:
            form = EmailPostForm()
        return render(request, 'bloggie/post/share.html', {'post': post,
                                                            'form': form})


