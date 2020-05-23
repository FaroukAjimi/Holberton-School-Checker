#!/usr/bin/python3
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout


class Brand(BoxLayout):
    """
    Displays Holberton School logo
    """
    def __init__(self, **kwargs):
        super(Brand, self).__init__(**kwargs)
        self.pos = 0, 200
        self.image = Image(source='project/assets/img/holbertonschool.png')
        self.add_widget(self.image)
