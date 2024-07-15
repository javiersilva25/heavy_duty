from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')

    def add_item(self, item, quantity=1):
        cart_item, created = CartItem.objects.get_or_create(cart=self, item=item)
        if not created:
            cart_item.quantity += quantity
        cart_item.save()
        return cart_item

    def remove_item(self, item):
        cart_item = CartItem.objects.get(cart=self, item=item)
        cart_item.delete()

    def clear_cart(self):
        self.cartitem_set.all().delete()

    def get_total_price(self):
        total = sum(item.item.price * item.quantity for item in self.cartitem_set.all())
        return total

    def __str__(self):
        return f'Cart of {self.user.username}'

    class Meta:
        ordering = ['user']

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.name} in {self.cart.user.username}\'s cart'

    class Meta:
        ordering = ['cart', 'item']

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
