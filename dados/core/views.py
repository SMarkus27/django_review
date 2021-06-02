from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404, reverse
from plotly.offline import plot
import pandas as pd
import plotly.express as px
from .models import Todo
from .forms import TaskForm


def index(request):
    tasks = Todo.objects.order_by('status')
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)


def one_task(request, id):
    tasks = get_list_or_404(Todo, id=id)
    context = {
        'tasks': tasks
    }
    return render(request, 'task.html', context)


def create_task(request):
    title = 'Create'
    form = TaskForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'edit.html', context)


def update_task(request, id):
    title = 'Update'
    task = get_object_or_404(Todo, id=id)
    form = TaskForm(request.POST or None, instance=task)
    print('update1')
    if request.method == 'POST':
        print('Update2')
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        'title': title,
        'form': form
    }
    return render(request, 'edit.html', context)


def delete_task(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('/')


def grafico(request):
    df_covid = pd.read_csv(
        "/home/marcus/Desktop/Tudo/Programacao/Data/dados/Jupyter/covid/caso_full.csv")
    df_covid = df_covid.dropna()
    df_cities = df_covid.groupby('state')
    df_new_deaths = df_cities['new_deaths'].sum().sort_values()
    fig = px.bar(df_new_deaths)
    fig.update_layout(title='N° de Morte por Estados',
                      xaxis=dict(title='Estados'),
                      yaxis=dict(title='N° total de Casos'),
                      legend_title_text='Legenda')
    fig.update_traces(name='Mortes')
    plot_div = plot(fig, output_type='div')
    context = {
        'plot_div': plot_div
    }
    return render(request, 'graficos.html', context)
