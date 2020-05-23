import requests
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from project import sm


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.xau = None
        self.pos = 100, 20
        self.size_hint = 0.7, 0.5
        self.cols = 2
        self.add_widget(Label(text='Email'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.add_widget(Label(text='API key'))
        self.api = TextInput(multiline=False)
        self.add_widget(self.api)

        self.notification = (Label(text='Status: not connected'))
        self.add_widget(self.notification)

        self.submit = Button(text='Connect', font_size=14)
        self.submit.bind(on_press=self.LoginCallback)
        self.add_widget(self.submit)

    def LoginCallback(instance, value):
        """
        Getting the authentification token
        """
        email = instance.username.text
        password = instance.password.text
        api = instance.api.text

        url = 'https://intranet.hbtn.io/users/auth_token.json'
        myobj = {"api_key": api, "email": email,
                 "password": password, "scope": "checker"}
        x = requests.post(url, data=myobj)
        xj = x.json()
        try:
            App.xau = xj['auth_token']  # authentification key
            msg = "Authentification success!"
            sm.current = "Project"
        except:
            msg = "Make sure your email \nor password are correct"
        instance.notification.text = msg
