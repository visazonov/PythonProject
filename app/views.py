from django.shortcuts import render

import netmiko
import os

# from dotenv import load_dotenv
# load_dotenv()
from netmiko import ConnectHandler

# from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import reverse


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Создать пользователя': reverse('create_user'),
        # 'Удалить пользователя': reverse('delete'),
    }

    context = {
        'pages': pages,
        'create_user_url': pages['Создать пользователя'],
    }
    return render(request, template_name, context)


def create_user(request):

    login = request.POST.get('login')
    password = request.POST.get('password')


    mikrotik_router_021 = {
        'device_type': 'mikrotik_routeros',
        'host': '192.168.1.1',
        'port': '22',
        'username': 'admin+ct',
        'password': 'admin'
    }

    sshCli = ConnectHandler(**mikrotik_router_021)
    # print(sshCli.find_prompt())
    prompt = sshCli.find_prompt()
    print(f'Prompt: {prompt}')
#
    commands = [
        f':global Vuser {login}',
        f':global password {password}',
        # '/system/script/run script1'
    ]
    for cmd in commands:
        output = sshCli.send_command(cmd, expect_string=r'>', delay_factor=2, read_timeout=60)

    sshCli.disconnect()

    return HttpResponse(f"Пользователь {login} успешно создан!")
    # return HttpResponse("Метод не поддерживается", status=405)
    # return HttpResponseRedirect(reverse('home'))




