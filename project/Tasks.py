#!/usr/bin/python3
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from project import App


class Tasks(GridLayout):
    """
    Tasks Screen handler
    """
    def __init__(self, **kwargs):
        super(Tasks, self).__init__(**kwargs)
        self.pos = 0, 20
        self.size_hint = 1, 0.5
        self.tasks = App.tasks

    def render(self):
        """
        printing The result
        """
        c = App.tasks
        self.cols = 5
        i = 0
        try:
            while c['result_display']['checks'][i]:
                for key, value in (c['result_display']['checks'][i]).items():
                    if key == 'passed':
                        if value is True:
                            checkerText = '[color=008000]Checker {}[/color]'\
                                .format(i)
                        else:
                            checkerText = '[color=ff3333]Checker {}[/color]'\
                                .format(i)
                        self.checker = Label(text=checkerText, markup=True)
                        self.add_widget(self.checker)
                i = i + 1
        except IndexError:
            pass
