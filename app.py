from flask import Flask, render_template
import requests
apiKey = 'efabeec0700c68be97e8a97c342ea5e1'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return 'Welcome to the weather app'

@app.route('/weather')
def weather():
    # Replace YOUR_API_KEY with the actual API key obtained from OpenWeatherMap
    url = f'https://api.openweathermap.org/data/2.5/weather?lat=57&lon=-2.15&appid={apiKey}&units=metric'


    # Fetch the data from the API
    response = requests.get(url)
    data = response.json()

    # Extract relevant data from the API response
    description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']

    # Return the weather data in the response
    # return f'{city} weather: {description}, Temperature: {temperature} C, Humidity: {humidity}%'
    return render_template('weather.html')
    
if __name__ == '__main__':
    app.run()