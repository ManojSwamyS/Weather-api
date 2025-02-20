import requests

API_KEY = '0bfcf83d06614df2876a11eba37a871a'
CITY = input("Enter city name:")

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    print(f"Weather in {CITY}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
else:
    print("City not found!")
