from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decoratots import *

# Create your views here.

@login_required(login_url='login')
def home(request):
    tasks = request.user.userdata.task_set.all()
    # user = UserData.objects.get(id=pk)

    todo = tasks.filter(status='To do')
    inProgress = tasks.filter(status='In progress')
    done = tasks.filter(status='Done')

    teams = Teams.objects.filter(users=request.user.id)

    context = {'team': team, 'todo': todo, 'inProgress': inProgress, 'done': done, 'teams': teams}
    return render(request, 'WP/home.html', context=context)

def newTask(request):

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        #form.fields['user'] = request.user
        if form.is_valid():
            saving = form.save(commit=False)
            saving.user = request.user.userdata
            saving.save()
            form.save()
            return redirect('/')

    teams = Teams.objects.all()
    context = {'form': form, 'teams': teams}

    return render(request, 'WP/newTask.html', context=context)


@login_required(login_url='login')
def backlog(request):
    return render(request, 'WP/backlog.html')


@login_required(login_url='login')
def report(request):
    return render(request, 'WP/report.html')


@login_required(login_url='login')
def team(request, pk):
    team = Teams.objects.get(id=pk)

    todo = team.task_set.filter(status='To do')
    inProgress = team.task_set.filter(status='In progess')
    done = team.task_set.filter(status='Done')

    teams = Teams.objects.all()

    context = {'team' : team, 'todo' : todo, 'inProgress': inProgress, 'done': done, 'teams' : teams}
    return render(request, 'WP/home.html', context=context)

# @login_required(login_url='login')
# def userPage(request):
#     tasks = request.user.userdata.task_set.all()
#     # user = UserData.objects.get(id=pk)
#
#     todo = tasks.filter(taskStatus='To do')
#     inProgress = tasks.filter(taskStatus='In progess')
#     done = tasks.filter(taskStatus='Done')
#
#     teams = Teams.objects.all()
#
#     context = {'team' : team, 'todo' : todo, 'inProgress': inProgress, 'done': done, 'teams' : teams}
#     return render(request, 'WP/home.html', context=context)


@login_required(login_url='login')
def updateTask(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.user = request.user.userdata
            saving.save()
            form.save()
            return redirect('/')
    teams = Teams.objects.all()

    context = {'form': form, 'teams' : teams}
    return render(request, 'WP/newTask.html', context=context)

@unauthenticated_user
def register(request):

    reg = CreateUserForm()

    if request.method == "POST":
        reg = CreateUserForm(request.POST)
        if reg.is_valid():
            user = reg.save()

            UserData.objects.create(
                user=user,
                username=reg.cleaned_data.get('username'),
                email=reg.cleaned_data.get('email')
            )

            messages.success(request, 'Account was created for ' + reg.cleaned_data.get('username'))
            return redirect('/log-in/')
    context = {'reg': reg}
    return render(request, 'WP/register.html', context=context)

@unauthenticated_user
def logIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        log = authenticate(request, username=username, password=password)
        if log is not None:
            login(request, log)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is inncorrect')
            return render(request, 'WP/login.html')

    context = {}
    return render(request, 'WP/login.html', context=context)

def logOut(request):
    logout(request)
    return redirect('login')

