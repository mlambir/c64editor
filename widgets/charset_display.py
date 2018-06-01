import numpy
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.gridlayout import GridLayout

from widgets.char_display import CharDisplay


class CharsetDisplay(GridLayout):
    charset = StringProperty('')
    fg_color = NumericProperty(0)
    bg_color = NumericProperty(0)

    def __init__(self, **kwargs):
        super(CharsetDisplay, self).__init__(**kwargs)
        self.chars = []
        for i in range(256):
            cd = CharDisplay()
            self.chars.append(cd)
            cd.fg_color = self.fg_color
            cd.bg_color = self.bg_color
            self.add_widget(cd)

    def on_bg_color(self, *args):
        for char in self.chars:
            char.bg_color = self.bg_color

    def on_fg_color(self, *args):
        for char in self.chars:
            char.fg_color = self.fg_color

    def on_charset(self, *args):
        barr = numpy.fromfile(self.charset, dtype=numpy.ubyte)
        barr = barr[1:]
        char_arrs = numpy.split(barr, len(barr) / 8)

        for i, char in enumerate(self.chars):
            if i < len(char_arrs):
                char.binary_char_data = reversed(char_arrs[i])
            else:
                char.binary_char_data = b''
