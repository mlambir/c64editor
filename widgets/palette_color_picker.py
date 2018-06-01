from kivy.app import App
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class PaletteButton(Button):
    color = ListProperty([1,1,1])
    index = NumericProperty()


class PaletteColorPicker(BoxLayout):
    selected_color = NumericProperty()

    def __init__(self, **kwargs):
        super(PaletteColorPicker, self).__init__(**kwargs)

        app = App.get_running_app()
        for i, color in enumerate(app.COLOR_PALETTE):
            btn = PaletteButton()
            btn.color = color
            btn.index = i
            def btn_press(pressed_button):
                self.selected_color = pressed_button.index
            btn.bind(on_press=btn_press)
            self.add_widget(btn)
