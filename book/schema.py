import graphene

import Autor.schema


class Query(Autor.schema.Query, graphene.ObjectType):
    
    pass

schema = graphene.Schema(query=Query)
