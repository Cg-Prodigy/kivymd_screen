from kivy.uix.screenmanager import Screen,ScreenManager,WipeTransition
from kivymd.uix.floatlayout import MDFloatLayout


class SwitchScreens(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition=WipeTransition()
    def change_screen(self):
        print('Changing screen')
class MainScreen(Screen):
  pass
class SignUpScreen(Screen):
    pass
class LoginScreen(Screen):
    pass