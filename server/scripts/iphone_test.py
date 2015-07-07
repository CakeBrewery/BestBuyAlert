from bba_server.models import Product, Watcher
from bba_server.serializers import WatcherSerializer
import requests
import json

#fields = ('name', 'status', 'purchase', 'target_price', 'products')

current_watcher = Watcher(name='iPhone', target_price='400')
current_watcher.save()


r = requests.get("http://api.remix.bestbuy.com/v1/products(name=iPhone*)?show=sku,name,regularPrice,salePrice&pageSize=15&page=5&apiKey=xkuweuxjvtgpnpv2vs5usq35&format=json")
response = r.json()


for p in list(response['products']):
	product = Product(
				name=p['name'], 
				lowest_price=min(p['regularPrice'],p['salePrice']), 
				watcher=current_watcher)
	product.save()

