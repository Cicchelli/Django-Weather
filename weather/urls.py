from django.urls import path

from weather.views import index, city_weather, weather_details

urlpatterns = [
    path("", index, name="home-page"),
    path("weather/<str:city>", city_weather, name="city-weather"),
    path(
        "weather/<str:city>/<str:target>",
        weather_details,
        name="weather-details",
    ),
]
