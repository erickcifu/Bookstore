import graphene
import Autores.schema

class Query(Autores.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
