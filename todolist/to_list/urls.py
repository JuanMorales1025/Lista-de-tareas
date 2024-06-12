from django.urls import path # type: ignore
from to_list.views import VerlistaView, CrearTareaView, EliminarTareaview
urlpatterns =[
    path('',VerlistaView.as_view(),name = "ver_lista"),
    path('crear/', CrearTareaView.as_view(),name ="crear_tarea"),
    path('eliminar/<int:pk>/',EliminarTareaview.as_view(), name = 'eliminar_tarea')
]

