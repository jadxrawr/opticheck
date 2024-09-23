from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
Window.size = (310, 580)

class OptiCheck(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("resetpass.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("resetpass.kv"))
        screen_manager.add_widget(Builder.load_file("testry.kv"))
        return screen_manager

if __name__ == '__main__':
    LabelBase.register(name="MPoppins", fn_regular="D:\Poppins\Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="D:\Poppins\Poppins-SemiBold.ttf")
    OptiCheck().run()