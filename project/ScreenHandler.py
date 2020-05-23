#!/usr/bin/python3
from project import sm, Screen
from kivy.lang.builder import Builder
from project import Brand
from project import LoginScreen
from project import Project
from project import Tasks


Builder.load_string("""
<ConnectionScreen>:
    Brand
    LoginScreen
<ProjectScreen>:
    Brand
    Project
<TasksScreen>:
    on_enter:
        self.render()
    Brand
""")


class ConnectionScreen(Screen):
    pass


class ProjectScreen(Screen):
    pass


class TasksScreen(Screen):
    def render(self):
        widget = Tasks.Tasks()
        widget.render()
        self.add_widget(widget)
    pass
sm.add_widget(ConnectionScreen(name="Connect"))
sm.add_widget(ProjectScreen(name="Project"))
sm.add_widget(TasksScreen(name="Tasks"))
