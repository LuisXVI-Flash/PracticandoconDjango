"""proyectoxd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('cursos/',views.cursos, name="cursos"),
    path('carreras/',views.carreras, name="carreras"),
    path('estudiantes/',views.estudiantes, name="estudiantes"),
    path('consultas/',views.consultas, name="consultas"),
    path('eliminar_cursos/<int:id>',views.eliminar_cursos, name="eliminar_cursos"),
    path('eliminar_carreras/<int:id>',views.eliminar_carreras, name="eliminar_carreras"),
    path('eliminar_estudiantes/<int:id>', views.eliminar_estudiantes, name="eliminar_estudiantes"),
    path('agregar_carrera/', views.agregar_carrera, name="agregar_carrera"),
    path('save-carrera/', views.save_carrera, name="save_carrera"),
    path('agregar_estudiante/', views.agregar_estudiante, name="agregar_estudiante"),
    path('save-estudiante/', views.save_estudiante, name="save_estudiante"),
    path('agregar_cursos/',views.agregar_cursos, name="agregar_cursos"),
    path('save-cursos/', views.save_cursos, name="save_cursos"),

]
