#!/usr/bin/env python3
"""
'schema' defines the structure of operations permitted on this GraphQL API
"""
import graphene
from graphene import Field, List, String, ID, Int, Float
from .models import Customer, Product, Order
from .types import CustomerType, ProductType, OrderType
from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils.timezone import now
import re


# -------------------------------------------
# Class defining API's 'read operations'
# -------------------------------------------
class Query(graphene.ObjectType):
    """Collection of 'read commands' (Fields) and associated logic (resolvers).
    Could also be defined as:
    	'class Query(CRMQuery, graphene.ObjectType)'
    Args:
    	graphene.ObjectType: Contains boilerplate connecting client and server side.
    """

    hello = graphene.String()

    def resolve_hello(root, info):
        """Resolver for any 'hello' request client-side.
        Args:
        	root: Represents the current instanciation of this Query class.
        	info: Contains useful context associated with the request made.
        Return:
        	A string representing the expected response.
        """
        return 'Hello, GraphQL!'


# -------------------------------------------
# The contract between client and server.
# define root query type and mutations
# -------------------------------------------
schema = graphene.Schema(query=Query)
