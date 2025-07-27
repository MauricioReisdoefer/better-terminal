import time
from betterterminalcli.core.screen_buffer import ScreenBuffer
from betterterminalcli.widgets.base_widget import BaseWidget
class TerminalApp:
    """
    Controla a renderização completa do terminal.
    """
    def __init__(self, width=70, height=30, fps:float=30):
        self.buffer = ScreenBuffer(width, height)
        self.widgets:list[BaseWidget] = []
        self.running = False
        self.fps = fps

    def add_widget(self, widget:BaseWidget):
        self.widgets.append(widget)

    def remove_widget(self, widget:BaseWidget):
        if widget in self.widgets:
            self.widgets.remove(widget)

    def draw_widgets(self):
        for widget in self.widgets:
            widget.render(self.buffer)

    def _update_widgets(self, dt: float):
        for widget in self.widgets:
            has_changed = widget.update(dt)
            if has_changed: self.draw_single_widget(widget)
                
    def draw_single_widget(self, widget:BaseWidget):
        widget.render(self.buffer)
    
    def show_widgets(self):
        for i, widget in enumerate(self.widgets):
            print(f"Widget {i} : {widget.name}")

    def run(self, draw_border: bool = True):
        raise NotImplementedError("Não Existe um Método Run Ainda")

    def stop(self):
        self.running = False
