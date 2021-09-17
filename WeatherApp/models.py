from django.db import models

# Create your models here.

class Cities(models.Model):
    Id = models.IntegerField(primary_key=True);
    Name = models.CharField(max_length = 100);
    State = models.CharField(max_length = 100, null=True);
    Country = models.CharField(max_length = 100);
    Longitude = models.FloatField();
    Latitude = models.FloatField();

class SearchHistory(models.Model):
    Id = models.AutoField(primary_key=True);
    CityName = models.CharField(max_length = 100);
    Temperature = models.CharField(max_length = 100, null=True);
    Icon = models.CharField(max_length = 100);
    TempCondition = models.CharField(max_length = 100);
    SearchDate = models.CharField(max_length = 10);
    SearchTime = models.CharField(max_length = 10);
    IsDay = models.BooleanField(default=False);