
from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='blog'),
    path('about.html', views.about, name='sobremi'),
    path('contact.html', views.contact, name='contact'),
    path('post.html', views.post, name='post'),
    path('trabajos.html', views.trabajos, name='trabajos'),
    path('alta_trabajo', views.alta_trabajo),
    path('alta_contacto', views.alta_contacto),
    path('busquedaTrabajos', views.busquedaTrabajos, name="BusquedaTrabajos"),
    path('buscar/', views.buscar),
]