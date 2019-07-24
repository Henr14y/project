from flask import Flask, render_template, redirect, url_for, request 
import math, requests, json
from twilio.rest import Client

app = Flask(__name__)

def get_weather(city_name):
	api_key = "d417dc0551776c3b502268c6c258dafb"
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



def sms(city1,temp1,humid1,pres1):
	account_sid = 'AC1aee1a7a3584630924166759198cfe43'
	auth_token = '78d4869f364a22da940f2cbcfe3a92ad'
	client = Client(account_sid, auth_token)

	message = client.messages \
                	.create(
                     		body="In " +city1 +", the temperature is " +str(temp1) +" celcuis, humidity is " +str(humid1) +" percent and pressure is " +str(pres1) +" Pascal.",
                     		from_='+12562578784',
                     		to='+233201895736'
        		         )
	



@app.route('/')
def index(city="Accra"):
	temp, humidity, pressure = get_weather(city)
	sms(city,temp,humidity,pressure)
	return render_template('home.html',c=city, t=temp, h=humidity, p=pressure)

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['search']
	print(text)
	return index(text)

@app.route('/test')
def test():
	city = my_form_post
	temp, humidity , pressure = get_weather(city)
	return render_template('home.html',t=temp, h=humidity, p=pressure)


if __name__== '__main__':
        app.run(debug = True, host = '0.0.0.0')








