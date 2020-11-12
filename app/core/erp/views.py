from django.shortcuts import render
from core.erp.models import *
from datetime import datetime


# Metodo me trae y renderiza el body html y los objectos que le envio
def home(request):
    carousel_active = Carousel.objects.all()[0:1]  # Me permite mostrar el primer elemento de mi carousel
    carousel_item = Carousel.objects.all()[1:]  # Me permite mostrar los elementos que pertenecen al carousel siguientes
    #sport_active = Sport.objects.all()  # .filter(sport__contains='CICLISMO') # Me permite traer los deportes registrado.
    category_all = Category.objects.all()  # Me permite listar todas las categorias
    type_product = TypeProduct.objects.all()  # Me permite traer los elementos tipo producto
    personal = Personal.objects.all()[0:3] # Me trae los 3 primeros elementos del personal
    personal_item = Personal.objects.all()[3:]
    return render(request, 'body.html', {
        'carousel_active': carousel_active,
        'carousel_item': carousel_item,
        'category_all': category_all,
        'type_product': type_product,
        'personal': personal,
        'personal_item': personal_item,
    })

