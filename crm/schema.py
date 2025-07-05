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


# ---------------------------------------------------------
# Mutation Field for simple 'create' on Customer table
# ---------------------------------------------------------
class CreateCustomer(graphene.Mutation):
    """Contains the logic for creation of a customer record. A bit like a 'Query resolver'.
    Inheritance:
    	graphene.Mutation: Enables customization of the mutation.
    """
    class Arguments:
        """Inner class for definition of the expected request inputs.
        """
        name = String(required=True)
        email = String(required=True)
        phone = String()


    customer = Field(CustomerType)
    success = graphene.Boolean()
    message = String()

    def mutate(self, info, name, email, phone=None):
        """Executes the CRUD operation on the database.
        Args:
        	self: Represents the current instance of this class.
        	info: An object containing additional context associated with the current request.
        	name: A required string object representing the new customer's name.
        	email: A required string object representing the new customer's email.
        	phone: Optional string representing the customer's phone number.
        """
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return CreateCustomer(success=False,
                                  message="Invalid email format")

        if phone and re.match(r"^(\+\d{1,3}\d{4,14}|(\d{3}-\d{3}-\d{4}))$", phone):
            return CreateCustomer(success=False,
                                  message="Invalid phone format")

        if Customer.objects.filter(email=email).exists:
            return CreateCustomer(success=False,
                                  message="Email already exists")

        customer = Customer(name=name, email=email, phone=phone)
        customer.save()
        return CreateCustomer(success=True,
                              message="Customer created",
                              customer=customer)


# ------------------------------------------------
# Class defining the API's 'read operations'
# ------------------------------------------------
class Query(graphene.ObjectType):
    """Collection of 'read commands' (Fields) and associated logic (resolvers).
    Could also be defined as:
    	'class Query(CRMQuery, graphene.ObjectType)'
    Inheritance:
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


# -----------------------------------------------
# Class defining the API's 'write operations'
# -----------------------------------------------
class Mutation(graphene.ObjectType):
    """Collection of 'write commands' (Fields) extracted from their 'resolvers'.
    Inheritance:
    	graphene.ObjectType: Contains boilerplate connecting client and server side.
    """
    create_customer = CreateCustomer.Field()


# -------------------------------------------
# The contract between client and server.
# Defines the root query type & mutations.
# -------------------------------------------
schema = graphene.Schema(query=Query)
