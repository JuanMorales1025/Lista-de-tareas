from django.shortcuts import render # type: ignore
from django.views.generic import ListView,CreateView, DeleteView, UpdateView# type: ignore
from to_list.models import ToDoItem
from to_list.forms import CrearTareaForm
from django.urls import reverse_lazy # type: ignore

# Create your views here.

class VerlistaView(ListView):
    model = ToDoItem
    template_name = 'listar_tareas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_tarea'] = ToDoItem.objects.all()
        return context

class CrearTareaView(CreateView):
    model = ToDoItem
    form_class = CrearTareaForm
    template_name = 'crear_tarea.html'
    success_url = reverse_lazy('ver_lista')

class EliminarTareaview(DeleteView):
    model = ToDoItem
    template_name = 'eliminar_tarea.html'
    success_url = reverse_lazy("ver_lista")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tarea'] = self.object
        return context

class EditarTareaView(UpdateView):
    model = ToDoItem
    template_name = "crear_tarea.html"
    form_class = CrearTareaForm
    success_url = reverse_lazy('ver_lista')

    def get_context_data(self, **kwargs):
        context = super(EditarTareaView,self).get_context_data(**kwargs)
        context['tarea'] = self.object
        return context