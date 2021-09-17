from django.conf.urls import url
from WeatherApp import views

urlpatterns =[
    url(r'^cities/$',views.getCities),
    url(r'^getSearchHistory/$',views.getSearchHistory),
    url(r'^addSearchHistory/$',views.addSearchHistory)
]