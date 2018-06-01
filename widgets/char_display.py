import numpy
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.instructions import Canvas
from kivy.graphics.texture import Texture
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.widget import Widget


class CharDisplay(Widget):
    binary_char_data = ListProperty([])
    fg_color = NumericProperty(0)
    bg_color = NumericProperty(1)

    def __init__(self, **kwargs):
        self.texture = Texture.create(size=(8, 8))
        self.texture.min_filter = 'nearest'
        self.texture.mag_filter = 'nearest'
        super(CharDisplay, self).__init__(**kwargs)

    def on_binary_char_data(self, *args, **kwargs):
        buf = []
        for b in numpy.unpackbits(self.binary_char_data):
            buf.append(255)
            buf.append(255)
            buf.append(255)
            buf.append(255 if b else 0)

        buf = bytes(buf)
        self.texture.blit_buffer(buf, colorfmt='rgba', bufferfmt='ubyte')

        self.draw()

    def draw(self):
        app = App.get_running_app()
        if not self.canvas:
            self.canvas = Canvas()
        self.canvas.clear()
        with self.canvas:
            Color(rgb=app.COLOR_PALETTE[self.bg_color])
            Rectangle(pos=self.pos, size=(self.width, self.height))
            Color(rgb=app.COLOR_PALETTE[self.fg_color])
            Rectangle(texture=self.texture, pos=self.pos, size=(self.width, self.height))
