import time
from betterterminalcli.core.screen_buffer import ScreenBuffer
from betterterminalcli.widgets.base_widget import BaseWidget
import threading
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
            has_changed, old_area = widget.update(dt)
            if has_changed: 
                
                x_start, y_start, x_end, y_end = old_area
                width = x_end - x_start
                height = y_end - y_start
                clear_matrix = [ [[" "] * width ] for _ in range(height)]
                self.buffer.draw_matrix(x_start, y_start, clear_matrix)
                
                self.draw_single_widget(widget)
                
                
    def draw_single_widget(self, widget:BaseWidget):
        widget.render(self.buffer)
    
    def show_widgets(self):
        for i, widget in enumerate(self.widgets):
            print(f"Widget {i} : {widget.name}")

    def run(self, draw_border: bool = True):
        try:
            self.running = True
            
            self.buffer.clear()
            self.buffer.os_clearterminal()
            
            last_time = time.time()
            while self.running:
                
                current_time = time.time()
                dt = current_time - last_time
                last_time = current_time

                self.draw_widgets()
                self._update_widgets(dt=dt)
                
                self.buffer.render(draw_border=draw_border)
                
                frame_time = time.time() - current_time
                sleep_time = max(0, (1 / self.fps) - frame_time)
                time.sleep(sleep_time)
        
        except KeyboardInterrupt:
            self.running = False
        
    def stop(self):
        self.running = False
