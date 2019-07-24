# -*-coding:utf8-*-
from django.shortcuts import render_to_response
from django.contrib import auth



def base(request):

    return render_to_response('base.html', locals())


def login(request):
    if request.POST and request.method == 'post':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = auth.authenticate(username=username,password=password)
        except ArithmeticError:
            return "username"


def logout(request):
    pass
