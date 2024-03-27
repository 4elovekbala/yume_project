from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(Product, related_name='orders')

    def __str__(self):
        return f"Order {self.pk}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    rental_duration = models.IntegerField()

    class Meta:
        unique_together = (('order', 'product'),)

    def __str__(self):
        return f"{self.product} in {self.order}"
