from django.shortcuts import render, HttpResponseRedirect
from user.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            email = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=email, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'Добро пожаловать, {user.first_name} {user.patronym}')
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)


@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        print("rnd")
        if form.is_valid():
            print("rnd")
            form.save()
            messages.success(request, 'Пользователь успешно добавлен')
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
