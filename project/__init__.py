#!/usr/bin/python3
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '300')
App.tasks = {}
App.xau = ""
# Create the manager
sm = ScreenManager()

from project import ScreenHandler


class MyApp(App):
    def build(self):
        print(sm.screens)
        return sm
