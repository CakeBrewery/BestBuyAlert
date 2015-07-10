from rest_framework import serializers
from bba_server.models import *


#A watcher is in charge of monitoring prices given some options
class WatcherSerializer(serializers.ModelSerializer):
	products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta: 
		model = Watcher
		fields = ('name', 'query_string', 'status', 'purchase', 'target_price', 'lowest_price', 'threshold', 'email', 'products', 'send_email')

#A product is one of possibly many products in the product pool of a watcher
class ProductSerializer(serializers.ModelSerializer): 

	class Meta : 
		model = Product
		fields = ('name', 'sku', 'lowest_price', 'watcher')
