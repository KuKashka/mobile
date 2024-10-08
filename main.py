from kivy.lang  import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screenmanager import MDScreenManager
import requests
from settings import *
#Ну прівєтікі

class WeatherScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def get_weather(self, city):
        params = {
            "q": city,
            "appid":API_KEY,
        }
        data = requests.get(CURRENT_WEATHER_URL,params)
        response = data.json()
        print(response)
        return response
    
    def search(self):
        city = self.ids.city.text
        weather = self.get_weather(city)
        
        temp = weather["main"]["temp"]
        self.ids.temp.text = f"{temp}°C"

        feels_like = weather["main"]["feels_like"]
        self.ids.feels_like.text = f"Відчуваєтся як {round(feels_like)}°C"


        desc = weather["weather"][0]["description"]
        self.ids.desc.text = desc.capitalize()


        humidity = weather["main"]["humidity"]
        self.ids.humidity.text = f"Вологість: {humidity}%"


        wind = weather["wind"]["speed"]
        self.ids.wind.text = f"Вітер: {wind} М/С"


        icon = weather["weather"][0]["icon"]
        self.ids.icon.source = f"https://openweathermap.org/img/wn/{icon}@2x.png"


    def show_Forecast(self):
        self.manager.transmitions.direction = 'right'
        self.maneger.current = 'forecast'

class Forecastscrean(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        def back(self):
            self.manager.transition.direction = 'right'
            self.manager.current = 'home'


class LCloudApp(MDApp):
    def build(self):
        Builder.load_file('style.kv')
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        sm = MDScreenManager()
        self.weather_screen =WeatherScreen(name='Home')
        self.forecast_screen = ForecastScreen(name='forecast')
        sm.add_widget(self.weather_screen_screen)
        sm.add_widget(self.forecast_screen_screen) 

        return WeatherScreen()
LCloudApp().run()