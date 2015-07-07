from django.db import models

# Create your models here.

STATUS_CHOICES = [(0,'OOS'),(1,'EXPENSIVE'),(2,'CHEAP'),(3,'BUY')]

class Watcher(models.Model):
	name = models.TextField()
	status = models.CharField(choices=STATUS_CHOICES, default='EXPENSIVE', max_length=16)
	purchase = models.BooleanField(default=False)
	target_price = models.DecimalField(max_digits=8, decimal_places=2)


class Product(models.Model):
	name = models.TextField()
	lowest_price = models.DecimalField(max_digits=8, decimal_places=2)
	watcher = models.ForeignKey(Watcher, related_name='products')
