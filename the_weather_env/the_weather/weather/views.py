from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import City
from .forms import CityForm

def delete_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    city.delete()
    return redirect('index')

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4ad71bf77fea6b62d9aa2203c9cb22da'

    cities = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : round((city_weather['main']['temp'] - 32) * 5/9),
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'max_temp' : round((city_weather['main']['temp_max'] - 32) * 5/9),
            'min_temp' : round((city_weather['main']['temp_min'] - 32) * 5/9),
        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weather/index.html', context)