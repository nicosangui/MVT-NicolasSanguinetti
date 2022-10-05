from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from familia.models import Persona


def crear_persona(request):
    persona1 = Persona(nombre='Romina', apellido='Zuñiga',fecha_de_creacion= datetime.now(), edad=32)
    persona1.save()

    persona2 = Persona(nombre='Rita', apellido='Parodi',fecha_de_creacion= datetime.now(), edad=54)
    persona2.save()

    persona3 = Persona(nombre='Jimena', apellido='Sanguinetti',fecha_de_creacion= datetime.now(), edad=28)
    persona3.save()

    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'personas' : persona1})
    template_renderizado = template.render({'personas' : persona2})
    template_renderizado = template.render({'personas' : persona3}) 
    return HttpResponse(template_renderizado)

def ver_personas(request):
    personas = Persona.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas}) 
   
    return HttpResponse(template_renderizado) 

