from django.shortcuts import render
from .forms import SignUpForm, LoginForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from .models import Profile

def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                print(key, value)
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return redirect(reverse('login'))
            user = User.objects.create_user(
                **{key: value for key, value in form.cleaned_data.items() if not key == 'passwordconf'})
            user.save()
            return redirect(reverse('login'))
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)
                next = request.GET.get('next', '/')
                return redirect(next)
            else:
                return redirect(reverse('login'))
    else:
        form = LoginForm()
    return render(request, 'login_user.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('home'))


@login_required
def profile_create(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        if profile:
            form = UserProfileForm(request.POST, request.FILES, instance=profile)
        else:
            form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        if profile:
            form = UserProfileForm(instance=profile)
        else:
            form = UserProfileForm()
    return render(request, 'profile_create.html', {'form': form})

