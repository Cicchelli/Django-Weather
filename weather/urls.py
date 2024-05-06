from django.urls import path

from weather.views import index, city_weather

urlpatterns = [
    path("", index, name="home-page"),
    path("weather/<str:city>", city_weather, name="city-weather"),
]
