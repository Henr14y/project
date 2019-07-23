from flask import Flask, render_template, redirect, url_for, request 
import math, requests, json

app = Flask(__name__)

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

else:
        print("City not found")






@app.route('/')
def index():
        return render_template('home.html',t=temp, h=humidity, p=pressure)



#@app.route('/index/<h>')
#def index1(h):
#        return render_template('home.html', h=humidity)

#@app.route('/index/<p>')
#def index2(p):
#        return render_template('home.html', p=pressure)

if __name__== '__main__':
        app.run(debug = True, host = '0.0.0.0')








