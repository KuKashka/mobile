from kivy.lang  import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screenmanager import MDScreenManager
import requests
from settings import *
from kivymd.uix.card import MDCard
#Ну прівєтікі

class WeatherScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city = 'Львів'


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
        weather = self.get_weather(self.city)
        
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


    def show_forecast(self):
        forecast_data = self.forecast.get_forecast(self.city)
        self.forecast.show_forecast(forecast_data)
        self.manager.transition.direction = 'right'
        self.manager.current = 'forecast'

class weatherCard(MDCard):
        def __init__(self, weather, *args, **kwargs):
            super().__init__(*args, **kwargs)
            temp = weather["main"]["temp"]
            icon = weather["weather"][0]["icon"]
            desc = weather["weather"][0]["description"]
            self.ids.desc.text = desc.capitalize()
            icon = weather["weather"][0]["icon"]
            self.ids.icon.source = f'https://openweathermap.org/img/wn/{icon}@2x.png'

class ForecastScrean(MDScreen):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.forecast = []

    def get_forecast(self, city):
        params = {
            "q": city,
            "appid":API_KEY,
        }
        data = requests.get(FORECAST_URL,params)
        response = data.json()
        print(response)
        return response ['list']
    
    def show_forecast(self, forecast):
        for data in forecast:
            card = weatherCard(data)  
            self.ids.weather_list.add_widget (card)


    def back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


class LCloudApp(MDApp):
    def build(self):
        Builder.load_file('style.kv')
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        sm = MDScreenManager()
        self.weather_screen =WeatherScreen(name='home')
        self.forecast_screen = ForecastScrean(name='forecast')
        self.weather_screen.forecast = self.forecast_screen
        sm.add_widget(self.weather_screen)
        sm.add_widget(self.forecast_screen) 

        return sm
LCloudApp().run()