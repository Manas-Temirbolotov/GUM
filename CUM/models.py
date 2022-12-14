from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    item_id = models.IntegerField()
    name = models.CharField(max_length=200)
    category_id = models.IntegerField()
    price = models.IntegerField()
    QR = models.CharField(max_length=20)

    def get_qr(self, item_id, price, category_id,):
        if category_id == 1:
            return f'{self.category_id} + "C" + {price} + "P" + {item_id} +"I"'
