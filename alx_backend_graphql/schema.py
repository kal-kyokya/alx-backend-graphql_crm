#!/usr/bin/env python3
"""
'schema' defines the structure of operations permitted on this GraphQL API
"""
import graphene
from crm.schema import Query as CRMQuery, Mutation as CRMMutation


# -------------------------------------------
# Class defining API's 'read operations'
# -------------------------------------------
class Query(CRMQuery, graphene.ObjectType):
    """Collection of 'read commands' (Fields) and associated logic (resolvers).
    Inheritance:
    	CRMQuery: Permitted queries to the 'crm App'.
    	graphene.ObjectType: Contains boilerplate enabling CRUD operations.
    """

    hello = graphene.String()

    def resolve_hello(root, info):
        """Resolver for any 'hello' request emerging from the client-side.
        Args:
        	root: Represents the current instanciation of this Query class.
        	info: Contains useful context associated with the request made.
        Return:
        	A string representing the expected response.
        """
        return 'Hello, GraphQL!'


# -------------------------------------------
# Class defining API's 'write operations'
# -------------------------------------------
class Mutation(CRMMutation, graphene.ObjectType):
    """Collection of 'write commands' (Fields) extracted from  their resolvers.
    Inheritance:
    	CRMMutation: Permitted modifications to the 'crm App'.
    	graphene.ObjectType: Contains boilerplate enabling CRUD operations.
    """
    pass


# -------------------------------------------
# The contract between client and server.
# define root query type and mutations
# -------------------------------------------
schema = graphene.Schema(query=Query, mutation=Mutation)
