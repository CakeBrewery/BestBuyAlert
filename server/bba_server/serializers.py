from rest_framework import serializers
from bba_server.models import *


#A watcher is in charge of monitoring prices given some options
class WatcherSerializer(serializers.ModelSerializer):
	products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta: 
		model = Watcher
		fields = ('name', 'status', 'purchase', 'target_price', 'products')

#A product is one of possibly many products in the product pool of a watcher
class ProductSerializer(serializers.ModelSerializer): 

	class Meta : 
		model = Product
		fields = ('name', 'lowest_price', 'watcher')
