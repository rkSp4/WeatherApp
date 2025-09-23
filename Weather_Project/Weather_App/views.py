from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .models import Search   # optional; remove if you didn't create models

def home(request):
    weather = None
    error = None
    city = ''
    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if city:
            api_key = getattr(settings, 'OPENWEATHER_API_KEY', '')
            if not api_key:
                error = "OpenWeather API key not configured on server."
            else:
                url = "https://api.openweathermap.org/data/2.5/weather"
                params = {
                    'q': city,
                    'appid': api_key,
                    'units': 'metric'  # use 'imperial' for Fahrenheit
                }
                try:
                    resp = requests.get(url, params=params, timeout=5)
                    resp.raise_for_status()
                    data = resp.json()
                    # Optionally save
                    try:
                        Search.objects.create(city=city, result_json=data)
                    except Exception:
                        pass
                    # Pick fields to display
                    weather = {
                        'city': f"{data.get('name')}, {data.get('sys', {}).get('country')}",
                        'description': data['weather'][0]['description'].title(),
                        'temp': data['main']['temp'],
                        'feels_like': data['main'].get('feels_like'),
                        'icon': data['weather'][0].get('icon'),
                    }
                except requests.exceptions.RequestException as e:
                    error = "Network error. Try again."
                except (KeyError, IndexError):
                    error = "Unexpected API response."
        else:
            error = "Please enter a city name."

    # For showing last 5 searches (optional)
    recent = Search.objects.order_by('-created_at')[:5] if 'Search' in globals() else []
    return render(request, 'weatherapp/home.html', {
        'weather': weather,
        'error': error,
        'city': city,
        'recent': recent
    })
