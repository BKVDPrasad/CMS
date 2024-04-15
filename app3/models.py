from django.db import models


# Create your models here.
class ItemMange(models.Manager):
    def active(self, *args, **kwargs):
        return self.filter(
            price=8.0,
            *args,
            **kwargs,
        )



class Item(models.Model):
    objects = ItemMange()
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)


class Item1(Item):
    val_of_item = models.CharField(max_length=64)