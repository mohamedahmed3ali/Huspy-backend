from rest_framework import serializers
from WeatherApp.models import Cities, SearchHistory

class CitiesSerializer(serializers.ModelSerializer):
    State = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Cities
        fields = ('Id',
                    'Name',
                    'State',
                    'Country',
                    'Longitude',
                    'Latitude')

class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = ('Id',
                    'CityName',
                    'Temperature',
                    'Icon',
                    'TempCondition',
                    'SearchDate',
                    'SearchTime',
                    'IsDay')