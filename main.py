
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDFillRoundFlatIconButton

Window.size = (310,580)

class Navbar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class MyToggleButton(MDFillRoundFlatIconButton, MDToggleButton):
    pass

class PBLApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        return screen_manager

LabelBase.register(name="MPoppins", fn_regular="C:\Windows\Fonts\Poppins-Medium.ttf")
LabelBase.register(name="BPoppins", fn_regular="C:\Windows\Fonts\Poppins-SemiBold.ttf")


PBLApp().run()