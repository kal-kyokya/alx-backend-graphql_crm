from django.db import models


# ---------------------------------------
# Collection of registered clients 
# ---------------------------------------
class Customer(models.Model):
    """Represents the DB table containing all customer informations.
    Inheritance:
    	models.Model: Base class enabling ORM management.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )


# ---------------------------------------
# Collection of offered products
# ---------------------------------------
class Product(models.Model):
    """Represents the Db table with all product records.
    Inheritance:
    	models.Model: Enables mapping of this class on the database.
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)


# ---------------------------------------
# Collection of all placed orders
# ---------------------------------------
class Order(models.Model):
    """Represents the Order table from the backend database.
    Inheritance:
    	models.Model: Ensures this class is mapped onto the right DB table.
    """
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
