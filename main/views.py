from curses.ascii import HT
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from main.utils import getStocks
import logging
logger = logging.getLogger('django')

@csrf_exempt
def index(request):
    content = json.loads(request.body)
    code = content['code']
    
    if request.method == 'GET':
        return HttpResponse("helloo")
    elif request.method == 'POST':
        try:
            stocks = getStocks(code)
        except Exception as e:
            logger.info(e.__str__())
            return HttpResponseBadRequest(e.__str__())
        return JsonResponse({'data':stocks})
    
    