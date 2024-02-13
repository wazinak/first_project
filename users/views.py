from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """регистрирует нового пользователя"""
    if request.method != 'POST':
        # выводит пустую строку
        form = UserCreationForm()
    else:
        # обработка заполненной информации
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # выполнение входа и перенаправление на домашнюю страницу
            login(request, new_user)
            return redirect('learning_logs:index')
    # вывести пустую или недействительную страницу
    context = {'form': form}
    return render(request,'registration/register.html', context)

