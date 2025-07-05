import graphene
from graphene_django import DjangoObjectType
from .models import Customer, Product, Order
from graphene import relay


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
        interfaces = (relay.Node,)
        filter_fields = ['name', 'email', 'phone', 'created_at']


class ProductType(DjangoObjectType):
    """Refers to the 'Product' table inside the database.
    Inheritance:
    	DjangoObjectType: Provides boilerplate simplifying CRUD operations.
    """
    class Meta:
        model = Product
        interfaces = (relay.Node,)
        filter_fields = ['name', 'price', 'stock']


class OrderType(DjangoObjectType):
    """Refers to the 'Order' table inside the database.
    Inheritance:
    	DjangoObjectType: Provides boilerplate simplifying CRUD operations.
    """
    class Meta:
        model = Order
        interfaces = (relay.Node,)
        filter_fields = ['total_amount', 'order_date']
