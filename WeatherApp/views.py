from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from WeatherApp.models import Cities, SearchHistory
from WeatherApp.serializers import CitiesSerializer, SearchHistorySerializer


# Create your views here.

@csrf_exempt
def getCities(request,city=''):
    if request.method =='GET':
        cities = Cities.objects.all()
        cities_serializer = CitiesSerializer(cities, many = True)
        return JsonResponse(cities_serializer.data, safe = False)

    elif request.method =='POST':
        json_city_data=JSONParser().parse(request)
        py_city_data = []
        for city in json_city_data:
            py_city_data.append({'Id': city['id'], 
                                    'Name': city['name'],
                                    'State': city['state'],
                                    'Country': city['country'],
                                    'Longitude': city['coord']['lon'],
                                    'Latitude': city['coord']['lat']})
        city_serializer = CitiesSerializer(data=py_city_data, allow_null=True, many=True)
        if city_serializer.is_valid():
            city_serializer.save()
            return JsonResponse("City added Successfully!!", safe=False)
        return JsonResponse("Failed to Add!!", safe=False)

# Search History services

@csrf_exempt
def getSearchHistory(request):
    if request.method =='GET':
        search_history = SearchHistory.objects.order_by('-Id')[:5]
        search_history_serializer = SearchHistorySerializer(search_history, many = True)
        return JsonResponse(search_history_serializer.data, safe = False)

@csrf_exempt
def addSearchHistory(request):
    if request.method =='POST':
        json_search_history_data=JSONParser().parse(request)
        search_history_serializer = SearchHistorySerializer(data=json_search_history_data, allow_null=True)
        
        if search_history_serializer.is_valid():
            search_history_serializer.save()
            return JsonResponse("City added Successfully!!", safe=False)
        return JsonResponse("Failed to Add!!", safe=False)