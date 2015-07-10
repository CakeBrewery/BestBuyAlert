from bba_server.models import Product, Watcher

import requests
import json

def update_prices():
	for product in Product.objects.all():
		api_string = "http://api.remix.bestbuy.com/v1/products(sku=" + product.sku + ")?show=sku,name,regularPrice,salePrice&apiKey=xkuweuxjvtgpnpv2vs5usq35&format=json"
		r = requests.get(api_string)
		response = r.json()

		product.lowest_price = min(response['products'][0]['regularPrice'],response['products'][0]['salePrice'])
		product.save()

	requests.get("http://localhost:8000/watchers/")