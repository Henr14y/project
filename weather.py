import requests, json , math

api_key = "d417dc0551776c3b502268c6c258dafb"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Accra"

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
        y = x["main"]
        temperature =  y["temp"]
        humidity = y["humidity"]
        pressure = y["pressure"]
        temp = math.floor(temperature - 273)

        print("Temperature: " +str(temp))
        print("Humidity: " +str(humidity))
        print("Pressure: " +str(pressure))

else:
        print("City not found")

