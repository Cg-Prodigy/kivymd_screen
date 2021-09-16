from kivy.factory import Factory
from kivy.core.window import Window
from kaki.app import App
from kivymd.app import MDApp

Window.size=(360,640)

class HotReload(App,MDApp):
    CLASSES={
        'SwitchScreens':'app.main_ui'
    }
    KV_FILES=[
        'app/kivy_lang.kv'
    ]
    AUTORELOADER_PATHS=[
        ('.',{'recursive':True})
    ]

    def build_app(self):
        return Factory.SwitchScreens()

if __name__=='__main__':
    HotReload().run()