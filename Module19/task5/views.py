from django.shortcuts import render
# плюс пэйджинатор и Post из моделей:
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage
from .models import Post

# Create your views here.

def post_list(request):
    # получаем все посты
    #posts = Post.objects.all()
    # или лучше с сортировкой (например, в обратном порядке от времени создания -created_at):
    posts = Post.objects.all().order_by('-created_at')

    # создаем пагинатор
    paginator = Paginator(posts, 4)  # 4 поста на странице

    # paginator.count -- число элементов в списке
    # paginator.num_pages -- число страниц (округление до большего)
    # paginator.page_range -- итератор для перебора номеров страниц

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')

    # получаем посты для текущей страницы
    page_posts = paginator.get_page(page_number)

    # передаем контекст в шаблон
    return render(request, 'task_19-5/post_list.html', {'page_posts': page_posts})


def post_list_with_check(request):
    # получаем все посты
    posts = Post.objects.all()

    # создаем пагинатор
    paginator = Paginator(posts, 3)  # количество постов на странице

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')

    # получаем посты для текущей страницы
    page_posts = paginator.get_page(page_number)

    page_number = request.GET.get('page')
    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, 'task_19-5/post_list.html', {'page_posts': page_posts})
