from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from bba_server.models import Product, Watcher
from bba_server.serializers import ProductSerializer, WatcherSerializer
from django.core.mail import send_mail

import requests
import json
from decimal import Decimal

# Create your views here.

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

def sendmail(watcher_purchase):
	email_list = set()
	for watcher in watcher_purchase:
		if (watcher.send_email):
			email_list.add(watcher.email)

	for email in email_list:
		product_alert = []
		for watcher in watcher_purchase:
			if (watcher.send_email and watcher.email == email):
				product_alert.append("[$" + str(watcher.lowest_price) + "] " + watcher.name)
				watcher.send_email = False
				watcher.save()
		send_mail('BBA - Purchase Alert', "\n".join(product_alert), 'no-reply@bba.com', [email], fail_silently=True)


@csrf_exempt
def watcher_list(request):
	"""
	List all watchers or create a new one
	"""
	if request.method == 'GET':
		for watcher in Watcher.objects.all(): 
			watcher.update()

		watcher = Watcher.objects.all()
		serializer = WatcherSerializer(watcher, many=True)

		watcher_purchase = Watcher.objects.all().filter(purchase=True)
		if (watcher_purchase):
			sendmail(watcher_purchase)

		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		#Grab Json data of desired products

		data = JSONParser().parse(request)

		query_string = data['query_string']
		target_price = Decimal(data['target_price'])
		threshold = Decimal(data['threshold'])
		email = data['email']
		send_email = data['send_email']

		api_string = "http://api.remix.bestbuy.com/v1/products(sku=" + query_string + ")?show=sku,name,regularPrice,salePrice&apiKey=xkuweuxjvtgpnpv2vs5usq35&format=json"

		r = requests.get(api_string)
		response = r.json()

		name = response['products'][0]['name']

		current_watcher = Watcher(name = name, query_string=query_string, target_price=target_price, threshold=threshold, email=email, send_email=(send_email=='True'))
		current_watcher.save()

		for p in list(response['products']):
			product = Product(
				name=p['name'], 
				lowest_price=min(p['regularPrice'],p['salePrice']), 
				watcher=current_watcher)
			product.save()

		return JSONResponse(data, status=201)
		"""
		serializer = WatcherSerializer(data=data)
		
		print serializer.is_valid()

		if serializer.is_valid():
			print serializer.data 
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		"""
		#return JSONResponse('error on POST request.method', status=400)

@csrf_exempt
def user_request(request):
	if request.method == "GET":
		return HttpResponse('')

	elif request.method == "POST":
		data = JSONParser().parse(request)
		return JSONResponse(data, status=200)
	