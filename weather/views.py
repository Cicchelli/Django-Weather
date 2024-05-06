from django.shortcuts import render

# Create your views here.
from weather.models import City, DailyWeather


def index(request):
    context = {"cities": City.objects.all()}
    return render(request, "home.html", context)


def city_weather(request, city):
    deslugified_city = city.replace("-", " ").title()

    queried_city = City.objects.get(name=deslugified_city)

    weathers = DailyWeather.objects.filter(city=queried_city)

    context = {"city": queried_city, "weathers": weathers}
    return render(request, "city_weather.html", context)
