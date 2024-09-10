import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        text = Label(text="Вітаю в мобільній розробці")
        btn = Button(text="Не натискай!")
        btn.on_press = self.btn_click
        col = BoxLayout(orientation="vertical")
        col.add_widget(text)
        col.add_widget(btn)
        return col

    def btn_click(self):
        print("А я казав")
        exit()
    
MyApp().run()