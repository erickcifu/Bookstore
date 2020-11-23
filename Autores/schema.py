import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from Autor.models import Libros, Autores

class LibrosNode(DjangoObjectType):
    class Meta:
        model = Libros
        filter_fields = ['name', 'Autores']
        interfaces = (relay.Node, )

# Se hace lo mismo con el modelo Ingredient
class AutorNode(DjangoObjectType):
    class Meta:
        model = Autor
        # Permite un filtrado mas avanzado
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'Libros': ['exact'],
            'Libros__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    Libros = relay.Node.Field(CategoryNode)
    all_libros = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(LibrosNode)
    all_autores = DjangoFilterConnectionField(AutortNode)
