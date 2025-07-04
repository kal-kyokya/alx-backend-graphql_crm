import graphene
from graphene_django import DjangoObjectType
from .models import Customer, Product, Order


# -----------------------------------------------
# Set of GraphQL's version of database tables
# -----------------------------------------------

class CustomerType(DjangoObjectType):
    """Refers to the 'Customer' table inside the database.
    Inheritance:
    	DjangoObjectType: Provides boilerplate simplifying CRUD operations.
    """
    class Meta:
        model = Customer


class ProductType(DjangoObjectType):
    """Refers to the 'Product' table inside the database.
    Inheritance:
    	DjangoObjectType: Provides boilerplate simplifying CRUD operations.
    """
    class Meta:
        model = Product


class OrderType(DjangoObjectType):
    """Refers to the 'Order' table inside the database.
    Inheritance:
    	DjangoObjectType: Provides boilerplate simplifying CRUD operations.
    """
    class Meta:
        model = Order
