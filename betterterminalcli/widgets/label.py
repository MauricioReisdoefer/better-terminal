from betterterminalcli.widgets import BaseWidget

class Label(BaseWidget):
    def __init__(self, text: str, x=0, y=0):
        super().__init__(x, y)
        self.text = text

    def render(self, buffer):
        buffer.draw(self.x, self.y, self.text)