from django.db import models
from operator import attrgetter
from decimal import Decimal 

#Options for status
STATUS_CHOICES = [(0,'OOS'),(1,'EXPENSIVE'),(2,'CHEAP'),(3,'BUY')]

#A watcher is in charge of monitoring prices given some options
class Watcher(models.Model):
	name = models.TextField()
	status = models.CharField(choices=STATUS_CHOICES, default='EXPENSIVE', max_length=16)
	purchase = models.BooleanField(default=False)
	target_price = models.DecimalField(max_digits=8, decimal_places=2)
	lowest_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
	threshold = models.DecimalField(max_digits=4, decimal_places=2, default=0.1)

	def update(self): 
		#Find current cheapest product from pool
		cheapest = min(self.products.all(), key=attrgetter('lowest_price'))
		print cheapest.name + ', ' + str(cheapest.lowest_price)

		self.lowest_price = cheapest.lowest_price

		if self.lowest_price <= self.target_price+self.target_price*Decimal(self.threshold):
			self.status = 'CHEAP'

			if self.lowest_price <= self.target_price:
				self.status = 'BUY'
				self.purchase = True

		self.save()


#A product is one of possibly many products in the product pool of a watcher
class Product(models.Model):
	name = models.TextField()
	lowest_price = models.DecimalField(max_digits=8, decimal_places=2)
	watcher = models.ForeignKey(Watcher, related_name='products')
