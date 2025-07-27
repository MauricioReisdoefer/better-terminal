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
        self.widgets.remove(widget)

    def draw_widgets(self):
        for widget in self.widgets:
            widget.render(self.buffer)

    def _update_widgets(self, dt: float):
        for widget in self.widgets:
            update = getattr(widget, "update", None)
            if callable(update):
                update(dt)

    def show_widgets(self):
        for i, widget in enumerate(self.widgets):
            print(f"Widget {i} : {widget.name}")

    def run(self, draw_border: bool = True):
        self.running = True
        frame_time = 1 / self.fps if self.fps else 0
        last = time.perf_counter()

        try:
            while self.running:
                now = time.perf_counter()
                dt = now - last
                last = now

                self.buffer.clear()
                self.buffer.os_clearterminal()
                self._update_widgets(dt)
                self.draw_widgets()
                self.buffer.render(draw_border=draw_border)

                if frame_time:
                    sleep_left = frame_time - (time.perf_counter() - now)
                    if sleep_left > 0:
                        time.sleep(sleep_left)
        except KeyboardInterrupt:
            pass
        finally:
            self.stop()


    def stop(self):
        self.running = False
