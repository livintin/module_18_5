# from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['user1', 'user2', 'user3']

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if int(age) < 18:
            info['error'] = "Вы должны быть старше 18."
        elif password != repeat_password:
            info['error'] = "Пароли не совпадают."
        elif username in users:
            info['error'] = "Пользователь с таким именем уже существует."
        else:
            users.append(username)
            return HttpResponse(f"Приветствуем, {username}!")

    return render(request, 'registration_page.html', info)



def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            age = form.cleaned_data['age']
            if password == confirm_password and age >= 18 and username not in users:
                return HttpResponse(f"Приветствуем, {username}!")
            else:
                info['error'] = "Пожалуйста, проверьте введенные данные."

            info['form'] = form
            return render(request, 'registration_page.html', info)