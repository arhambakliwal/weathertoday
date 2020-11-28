from django.shortcuts import render
import requests
import json
from .models import City
from .forms import CityForm
"""
def index(request):

    cities=City.objects.all()
    weather_data=[]
    for city in cities:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a4a8ed8028dda875b422cdef1662a5d6'

        r = requests.get(url.format(city)).json()
        city_weather = {'city': city,
                        'temperature': r['main']['temp'],
                        'mintemp': r['main']['temp_min'],
                        'maxtemp': r['main']['temp_max'],
                        'description': r['weather'][0]['description'],
                        'icon': r['weather'][0]['icon']
                        }
        weather_data.append(city_weather)
    x={'weather_data':weather_data}
    return render(request,'weather.html',x)

"""
def index(request):
    cities=City.objects.all()
    # cities=City.objects.all()
    if request.method=='POST':
        form=CityForm(request.POST)
        form.save()
    form=CityForm()


    weather_data=[]
    for city in cities:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a4a8ed8028dda875b422cdef1662a5d6'

        r = requests.get(url.format(city)).json()
        city_weather = {'city': city,
                        'temperature': r['main']['temp'],
                        'mintemp': r['main']['temp_min'],
                        'maxtemp': r['main']['temp_max'],
                        'description': r['weather'][0]['description'],
                        'icon': r['weather'][0]['icon']
                        }
        weather_data.append(city_weather)
    x={'weather_data':weather_data,'form':form}
    return render(request,'weather.html',x)
# Create your views here.
