from rest_framework import serializers
from bba_server.models import *


class WatcherSerializer(serializers.ModelSerializer):
	products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta: 
		model = Watcher
		fields = ('name', 'status', 'purchase', 'target_price', 'products')

class ProductSerializer(serializers.ModelSerializer): 

	class Meta : 
		model = Product
		fields = ('name', 'lowest_price', 'watcher')
