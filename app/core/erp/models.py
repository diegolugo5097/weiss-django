from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.
"""
Creacion de modelos Para el apartado de home/Primera etapa
"""


# Modelo de categoria de los deportes.
class Category(models.Model):
    name = models.CharField(verbose_name='Categoria', unique=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ' Categoria '
        verbose_name_plural = 'Categorias'
        ordering = ['id']


# Modelo del genero del personal de la empresa.
class Gender(models.Model):
    gender = models.CharField(verbose_name='Genero', unique=True, max_length=255)

    def __str__(self):
        return self.gender

    class Meta:
        verbose_name = ' Genero '
        verbose_name_plural = 'Generos'
        ordering = ['id']


# Modelo de carosel de la pagina.
class Carousel(models.Model):
    image = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Imagen', null=True)
    link = models.CharField(verbose_name='Link', max_length=1000, null=True)

    class Meta:
        verbose_name = ' Carousel '
        verbose_name_plural = 'Carousel'
        ordering = ['id']


# Modelo para la gestion del personal.
class Personal(models.Model):
    image = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Imagen', null=True)
    name_lastname = models.CharField(verbose_name='Nombre completo', max_length=255)
    position = models.CharField(verbose_name='Cargo', max_length=255)

    def __str__(self):
        return self.name_lastname

    class Meta:
        verbose_name = ' Personal '
        verbose_name_plural = 'Personal'
        ordering = ['id']


# Modelo para la gestion de deportes.
""""class Sport(models.Model):
    sport = models.CharField(verbose_name='Nombre', unique=True, max_length=255, null=True)
    image = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Imagen', null=True)

    def __str__(self):
        return self.sport

    class Meta:
        verbose_name = ' Deporte '
        verbose_name_plural = 'Deportes'
        ordering = ['id']
"""""
# Modelo para la gestion de tipos de productos
class TypeProduct(models.Model):
    name = models.CharField(verbose_name='Nombre', unique=True, max_length=255, null=True)
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Imagen', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ' Tipo de producto '
        verbose_name_plural = 'Tipos de producto'
        ordering = ['id']


# Modelo para la gestion de productos.
class Product(models.Model):
    typeProduct = models.ForeignKey(TypeProduct, verbose_name='Tipo de producto', on_delete=models.CASCADE, null=True)
    name = models.CharField(verbose_name='Nombre', unique=True, max_length=255, null=True)
    brand = models.CharField(verbose_name='Marca', max_length=255, null=True)
    image = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Imagen', null=True)
    description = RichTextField(verbose_name='Descripción', blank=True, null=True)
    price = models.DecimalField(verbose_name='Precio', max_length=9, max_digits=19, decimal_places=3, null=True)
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')
    availability = models.CharField(verbose_name='Disponiblidad', max_length=255, null=True)
    code_id = models.CharField(verbose_name='ID', unique=True, max_length=255, null=True)
    style = models.CharField(verbose_name='Estilo', max_length=255, null=True)
    product_condition = models.CharField(verbose_name='Condición del producto', max_length=255, null=True)
    register_date = models.DateField(verbose_name='Fecha de Registro/Modificiación', default=datetime.now)
    gender = models.ForeignKey(Gender, verbose_name='Genero', on_delete=models.CASCADE, null=True)
    specs = RichTextField(verbose_name='Especificaciónes', blank=True, null=True)

    def __str__(self):
        return f"NOMBRE: {self.name} // CANTIDAD: {self.quantity} // PRECIO: {self.price}"

    class Meta:
        verbose_name = ' Producto '
        verbose_name_plural = 'Productos'
        ordering = ['id']
