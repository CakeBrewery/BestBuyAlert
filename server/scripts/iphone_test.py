from bba_server.models import Product, Watcher
from bba_server.serializers import WatcherSerializer
import requests
import json

#Grab Json data of desired products
r = requests.get("http://api.remix.bestbuy.com/v1/products(name=iPhone*)?show=sku,name,regularPrice,salePrice&pageSize=15&page=5&apiKey=xkuweuxjvtgpnpv2vs5usq35&format=json")
response = r.json()



# Watcher #1: Instantiate a watcher for iPhone prices around 400 
current_watcher = Watcher(name='iPhone400', target_price='400')
current_watcher.save()

#turn json data into products for our watcher
for p in list(response['products']):
	product = Product(
				name=p['name'], 
				lowest_price=min(p['regularPrice'],p['salePrice']), 
				watcher=current_watcher)
	product.save()


# Watcher #2: Instantiate a watcher for Iphone prices around 680
current_watcher = Watcher(name='iPhone680', target_price='680')
current_watcher.save()

#turn json data into products for our watcher
for p in list(response['products']):
	product = Product(
				name=p['name'], 
				lowest_price=min(p['regularPrice'],p['salePrice']), 
				watcher=current_watcher)
	product.save()


# Watcher #3: Instantiate a watcher for Iphone prices around 680
current_watcher = Watcher(name='iPhone750', target_price='750')
current_watcher.save()

#turn json data into products for our watcher
for p in list(response['products']):
	product = Product(
				name=p['name'], 
				lowest_price=min(p['regularPrice'],p['salePrice']), 
				watcher=current_watcher)
	product.save()



