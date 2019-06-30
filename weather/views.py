import requests
from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request, 'weather/home.html')


def get_data(r):
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&APPID=7b917a51935f39b84c83478feb533bef'

        r = requests.get(url.format(r)).json()

        details = {
            'city': r['name'],
            'temp': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
    except:
        details = {}
    return details


def result(request):
    city = request.POST.get('city')

    data = get_data(city)

    context = {
        'city_weather': data
    }

    return render(request, 'weather/result.html', context)
