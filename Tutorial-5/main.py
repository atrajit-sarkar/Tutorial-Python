from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup



def printf(name):
    return f"My name is {name}"
class Mainscreen(Screen):
    def __init__(self, **kwargs):
        super(Mainscreen, self).__init__(**kwargs)

        self.takeinput=TextInput(hint_text="Enter your name")
        self.button1=Button(text="Click here")
        self.button1.bind(on_press=self.output)
        self.outputbox=TextInput(hint_text="Here is out put")
        


        self.layout=BoxLayout(orientation="vertical")
        self.layout.add_widget(self.takeinput)
        self.layout.add_widget(self.outputbox)
        self.layout.add_widget(self.button1)
        self.add_widget(self.layout)

    def output(self,a):
        str=printf(self.takeinput.text)
        self.outputbox.text=str
    

class Samaresh(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Mainscreen(name="Mainscreen"))

        return sm

Samaresh().run()



        
        
