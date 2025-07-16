from django.shortcuts import render

import netmiko
import os

# from dotenv import load_dotenv
# load_dotenv()
from netmiko import ConnectHandler

from django.http import HttpResponse
from django.shortcuts import render, reverse

from django.http import HttpResponse
from django.shortcuts import render, reverse

user_vpn = 'Testov53'
password_vpn = 'Test53'

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

    commands = [
        f':global Vuser {user_vpn}',
        f':global password {password_vpn}',
        '/system/script/run script1'
    ]
    for cmd in commands:
        output = sshCli.send_command(cmd, expect_string=r'>', delay_factor=2, read_timeout=60)

    sshCli.disconnect()

    msg = f'Пользователь login успешно создан'
    return HttpResponse(msg)

#kfjfj

