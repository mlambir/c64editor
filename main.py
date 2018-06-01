import os

import kivy
from kivy.app import App
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout


class MainWindow(BoxLayout):
    options = ListProperty([])
    selected_option = NumericProperty()

    def __init__(self, **kwargs):
        self.options = sorted(os.listdir('bins/charsets'))
        self.selected_option = 0
        super(MainWindow, self).__init__(**kwargs)


class C64EditorApp(App):
    COLOR_PALETTE = [
        kivy.utils.get_color_from_hex('#000000'),
        kivy.utils.get_color_from_hex('#FFFFFF'),
        kivy.utils.get_color_from_hex('#880000'),
        kivy.utils.get_color_from_hex('#AAFFEE'),
        kivy.utils.get_color_from_hex('#CC44CC'),
        kivy.utils.get_color_from_hex('#00CC55'),
        kivy.utils.get_color_from_hex('#0000AA'),
        kivy.utils.get_color_from_hex('#EEEE77'),
        kivy.utils.get_color_from_hex('#DD8855'),
        kivy.utils.get_color_from_hex('#664400'),
        kivy.utils.get_color_from_hex('#FF7777'),
        kivy.utils.get_color_from_hex('#333333'),
        kivy.utils.get_color_from_hex('#777777'),
        kivy.utils.get_color_from_hex('#AAFF66'),
        kivy.utils.get_color_from_hex('#0088FF'),
        kivy.utils.get_color_from_hex('#BBBBBB'),
    ]
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    C64EditorApp().run()
