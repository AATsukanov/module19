from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister
from .models import Game, Buyer

# Create your views here.
def platform(request):
    return render(request, 'task_19-3/platform.html')


def games(request):
    # games = ['Heroes of Might and Magic',
    #          'The Gothic',
    #          'The Kreed',
    #          'World Of Tanks']
    games = Game.objects.all()

    context = {'games': games}
    return render(request, 'task_19-3/games.html', context=context)


def cart(request):
    return render(request, 'task_19-3/cart.html')


def sign_up_by_html(request):
    # Псевдо-список users уже существующих пользователей:
    '''users = ['Alexey', 'Trump', 'Musk', 'JackieChan', 'vanDamme']'''
    users = Buyer.objects.all()

    info = {}

    if request.method == 'POST':
        # Получаем данные:
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        '''
        1.'Пароли не совпадают', если не совпали введённые пароли.
        2.'Вы должны быть старше 18', если возраст меньше 18.
        3.'Пользователь уже существует', если username есть в users.
        '''
        error_message = ''

        exists = False
        for u in users:
            if username == u.name:
                exists = True
        # if username in users:
        if exists:
            error_message += 'Пользователь уже существует\n'

        if password != repeat_password:
            error_message += 'Пароли не совпадают\n'
        try:
            age = int(age)
            if age < 18:
                error_message += 'Вы должны быть старше 18\n'
        except:
            error_message += 'Возраст должен быть целым числом\n'

        # для контроля:
        print('sign_up_by_html(request):')
        print(f'username = "{username}"')
        print(f'password = "{password}"')
        print(f'repeat_password = "{repeat_password}"')
        print(f'age = "{age}"')
        print(info)

        if not error_message:
            #users.append(username)
            Buyer.objects.create(name=username, balance=5550, age=age)
            # Http-ответ пользователю:
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            info['error'] = error_message
            return render(request, 'task_19-3/index.html', context=info)
    # если это GET:
    return render(request, 'task_19-3/registration_page.html')


def sign_up_by_django(request):
    # Псевдо-список users уже существующих пользователей:
    '''users = ['Alexey', 'Trump', 'Musk', 'JackieChan', 'vanDamme']'''
    users = Buyer.objects.all()

    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            # Обрабатываем данные формы:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            '''
            1.'Пароли не совпадают', если не совпали введённые пароли.
            2.'Вы должны быть старше 18', если возраст меньше 18.
            3.'Пользователь уже существует', если username есть в users.
            '''
            error_message = ''

            exists = False
            for u in users:
                if username == u.name:
                    exists = True
            # if username in users:
            if exists:
                error_message += 'Пользователь уже существует\n'

            if password != repeat_password:
                error_message += 'Пароли не совпадают\n'
            try:
                age = int(age)
                if age < 18:
                    error_message += 'Вы должны быть старше 18\n'
            except:
                error_message += 'Возраст должен быть целым числом\n'

            # для контроля:
            print('sign_up_by_django(request):')
            print(f'username = "{username}"')
            print(f'password = "{password}"')
            print(f'repeat_password = "{repeat_password}"')
            print(f'age = "{age}"')
            print(info)

            if not error_message:
                #users.append(username)
                Buyer.objects.create(name=username, balance=100000, age=age)
                # Http-ответ пользователю:
                return HttpResponse(f'Приветствуем, {username}!')
            else:
                info['error'] = error_message
                return render(request, 'task_19-3/index.html', context=info)
    else:
        # если это GET:
        form = UserRegister()
    return render(request, 'task_19-3/index_django.html', {'form': form})
