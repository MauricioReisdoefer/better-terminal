from typing import Optional
from betterterminalcli.core.screen_buffer import ScreenBuffer
from betterterminalcli.widgets.base_widget import BaseWidget

class TextWidget(BaseWidget):
    def __init__(self, text: str, x: int = 0, y: int = 0, name: Optional[str] = "TextWidget"):
        super().__init__(name=name, x=x, y=y)
        self.text = text
        self.width = len(text)

    def render(self, buffer: ScreenBuffer):
        buffer.draw(self.x, self.y, self.text)

    def update(self, dt: float) -> list[bool, list]:
        
        old_area = [self.x, self.y, self.x + self.width, self.y]
        
        self.width = len(self.text)
        return [True, old_area]

    def change_text(self, new_text):
        self.text = new_text