import Adafruit_DHT
import os
from flask import Flask, render_template, redirect, url_for, request 
import math, requests, json
from twilio.rest import Client

app = Flask(__name__)

def get_weather(city_name):
	#api_key = os.environ['weather_api_key'}
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name

	response = requests.get(complete_url)

	x = response.json()

	if x["cod"] != "404":
		y = x["main"]
		temperature =  y["temp"]
		humidity = y["humidity"]
		pressure = y["pressure"]
		temp = math.floor(temperature - 273)
		return temp, humidity, pressure

	else:
        	print("City not found")

def breadboard():
        sensor = Adafruit_DHT.DHT22
        pin = 4
        humidity1, temperature1 = Adafruit_DHT.read_retry(sensor, pin)

        temp1 = math.floor(temperature1)
        humid = math.floor(humidity1)

        return temp1,humid


def sms(city1,temp1,humid1,pres1, number):
	if number is None:
		return
	#account_sid = os.environ['twilio_account_ssid'}
	#auth_token = os.environ['twilio_auth_token'}
	client = Client(account_sid, auth_token)

	message = client.messages \
                	.create(
                     		body="In " +city1 +", the temperature is " +str(temp1) +" celcuis, humidity is " +str(humid1) +" percent and pressure is " +str(pres1) +" Pascal.",
                     		from_='+12162085631',
                     		to=number
        		         )
	



@app.route('/')
def index(city="Accra", pnumber=None):
	temp, humidity, pressure = get_weather(city)
	btemp,bhumidity = breadboard()
	sms(city,temp,humidity,pressure,pnumber)
	return render_template('home.html',c=city, t=temp, h=humidity, p=pressure, t1=btemp ,h1 =bhumidity, pn=pnumber)

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['search']
	number = request.form['numero']
	print(text, number)
	return index(text, number)

@app.route('/test')
def test():
	city = my_form_post
	temp, humidity , pressure = get_weather(city)
	return render_template('home.html',t=temp, h=humidity, p=pressure)


if __name__== '__main__':
        app.run(debug = True, host = '0.0.0.0')








