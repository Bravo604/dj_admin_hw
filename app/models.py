from django.db import models
from django.contrib import admin


class Block(models.Model):
    block_number = models.IntegerField()
    price = models.IntegerField()
    entrance_quantity = models.IntegerField()
    number_of_floors = models.IntegerField()
    number_of_apartments = models.IntegerField()

    def __str__(self):
        return f'{self.block_number}'


class Apartment(models.Model):
    STATUS_CHOICES = (
        ('sold', 'Выкуп'),
        ('credit', 'Выкуп не до конца'),
        ('cancel', 'Расторгнуто'),
        ('not sold', 'Не продано'),
    )
    owners_name = models.CharField(max_length=100, blank=True, null=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    date_purchase = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    area = models.IntegerField(default=100)

    def __str__(self):
        return f'{self.owners_name} - {self.block} - {self.status}'

