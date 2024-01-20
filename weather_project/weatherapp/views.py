from django.shortcuts import render
import requests
import datetime


def index(request):
    api_key = '39b2738f52e47a5759fbead880263f47'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    if request.method == 'POST':
        city1 = request.POST['city1']

        weather_data1 = fetch_weather(city1, api_key,current_weather_url)

        context = {
            'weather_data1': weather_data1,
        }

        return render(request, 'weather_app/index.html', context)
    else:
        return render(request, 'weather_app/index.html')


def fetch_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }



    return weather_data
