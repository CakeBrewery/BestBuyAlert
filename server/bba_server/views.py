from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from bba_server.models import Product, Watcher
from bba_server.serializers import ProductSerializer, WatcherSerializer

# Create your views here.

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)



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
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = WatcherSerializer(data=data)
		if serializer.is_valid(): 
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)
