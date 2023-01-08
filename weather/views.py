from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
import urllib.request

API_KEY = '736e57425abb7913cabbe7aebdb8fdbe'

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            res = urllib.request.urlopen('https://api.weatherapi.com/v1/current.json?key=0140716162d84ebbb06124344230801&q='+ city + '&aqi=yes')
        except:
            error = {
                'err_message': "Please, enter a valid city name!"
            }
            return render(request,'index.html',error)
        json_data = json.load(res)
        data = {
            'city':json_data['location']['name'],
            'country': json_data['location']['country'],
            'coordinate': str(json_data['location']['lon']) + ' ' + str(json_data['location']['lon']),
            'temperature': json_data['current']['temp_c'],
            'condition': json_data['current']['condition']['text'],
            'wind': json_data['current']['wind_kph'],
            'humidity': json_data['current']['humidity']
        }
        return render(request,'index.html', data)
    return render(request, 'index.html')

