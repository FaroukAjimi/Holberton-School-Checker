#!/usr/bin/python3
import requests
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.clock import Clock
from project import App, sm


class Project(BoxLayout):
    def __init__(self, **kwargs):
        super(Project, self).__init__(**kwargs)
        self.pos = 150, 30
        self.size_hint = 0.5, 0.5
        self.orientation = 'vertical'

        self.add_widget(Label(text='Project ID'))
        self.project_id = TextInput(multiline=False)
        self.add_widget(self.project_id)

        self.add_widget(Label(text='Task ID'))
        self.task_id = TextInput(multiline=False)
        self.add_widget(self.task_id)
        self.submit = Button(text='Request a correction', font_size=14)

        self.submit.bind(on_press=self.getProject)
        self.add_widget(self.submit)
        self.pb = ProgressBar(value=0, max=100)
        self.add_widget(self.pb)

    def getProject(instance, value):
        """
        Getting your project and the task informations
        """
        pid = instance.project_id.text
        tnumber = instance.task_id.text
        xau = App.xau

        proj = requests.get('https://intranet.hbtn.io/projects/{}\
.json?auth_token={}'.format(pid, xau))
        projj = proj.json()
        tid = projj['tasks'][int(tnumber)]['id']  # task ID
        """
        requesting a correction for The task
        """
        id = requests.post('https://intranet.hbtn.io/tasks/\
{}/start_correction.json?auth_token={}'.format(tid, xau))
        corrid = id.json()
        instance.cid = corrid['id']  # Correction Id
        Clock.schedule_interval(instance.increase_pb, 0.2)

    def requestCorrection(self, value):
        """
        Requestion our correction
        """
        xau = App.xau
        cid = self.cid
        corr = requests.get(
            'https://intranet.hbtn.io/correction_requests/{}\
.json?auth_token={}'.format(cid, xau))
        c = corr.json()
        App.tasks = c

    def increase_pb(self, value):
        self.pb.value += 1
        if (self.pb.value == 100):
            Clock.schedule_once(self.requestCorrection)
            Clock.unschedule(self.increase_pb)
            sm.current = "Tasks"
