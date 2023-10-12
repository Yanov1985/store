from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from user.models import User
from user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from demo.models import Basket
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем!Вы успешно зарегистировались!')
            return HttpResponseRedirect('/login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)

@login_required
def profile(request):
    form = None  # Инициализируем form значением None
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile')
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)
    total_sum = 0
    total_quantity = 0
    for basket in baskets:
        total_sum = total_sum + basket.sum()
        total_quantity = total_quantity + basket.quantity

    context = {'title': 'Профиль',
               'form': form,
               'baskets': baskets,
               'total_sum': total_sum,
               'total_quantity': total_quantity,
               }
    return render(request, 'user/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')