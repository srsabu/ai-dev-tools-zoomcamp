from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo

# Create your views here.

class TodoListView(ListView):
    model = Todo
    template_name = 'todoapp/todo_list.html'
    context_object_name = 'todos'
    ordering = ['-created_at']

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'description', 'due_date']
    success_url = reverse_lazy('todo_list')
    template_name = 'todoapp/todo_form.html'

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'description', 'due_date', 'is_resolved']
    success_url = reverse_lazy('todo_list')
    template_name = 'todoapp/todo_form.html'

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')
    template_name = 'todoapp/todo_confirm_delete.html'
