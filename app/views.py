from django.shortcuts import render

import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse

from django.http import HttpResponse
from django.shortcuts import render, reverse

def home_view(request):
    template_name = 'app/home.html'

    pages = {
        # 'Главная страница': reverse('home'),
        'Создать пользователя': reverse('time'),
        # 'Удалить пользователя': reverse('delete'),
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)



def create_user(request):

    msg = f'Пользователь login успешно создан'
    return HttpResponse(msg)


# def time_view(request):
#     current_time = datetime.datetime.now().time().strftime('%H:%M:%S')
#     msg = f'Пользователь login успешно создан'
#     return HttpResponse(msg)

