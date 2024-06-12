from django import forms  # type: ignore
from to_list.models import ToDoItem

class CrearTareaForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title','description']

        labels ={
            'title':'Titulo de la Tarea',
            'description':'Descripcion de la Tarea',
        }

        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo de la Tarea'}),
            'description': forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo de la Tarea'})
        }