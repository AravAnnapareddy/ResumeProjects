import requests

# pip install requests in terminal
API_KEY = "3bf81a057d8b6cc52f8dcd07b1229078"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# queery parameters: what cities we get weather data from

city = input("Enter a City name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"] - 273.15
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occured.")
