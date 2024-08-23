from django.contrib.auth.models import User
from django.db import models
from bookapp.models import Book
# Create your models here.



class Cart(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Book, through='CartItem')


    def __str__(self):
        return "{}".format(self.items)


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return "{}".format(self.cart)
