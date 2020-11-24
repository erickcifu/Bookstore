import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from Autores.models import Libros, Autores

class AutorNode(DjangoObjectType):
    class Meta:
        model = Autores
        filter_fields = {
        'name': ['exact', 'icontains', 'istartswith'],
            'Fecha_Nacimiento': ['exact'],
            'category': ['exact'],
            'category__name': ['exact'],
            }
        interfaces = (relay.Node, )

class LibrosNode(DjangoObjectType):
    class Meta:
        model = Libros
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'Fecha_creacion': ['exact'],
            'Descripcion':['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    Libros = relay.Node.Field(LibrosNode)
    all_libros = DjangoFilterConnectionField(LibrosNode)

    Autores = relay.Node.Field(AutorNode)
    all_autores = DjangoFilterConnectionField(AutorNode)
