from collections import defaultdict

class EventManager:
    def __init__(self):
        self.listeners = defaultdict(list)

    def on(self, event_name, callback):
        """Registra um listener para um evento"""
        self.listeners[event_name].append(callback)

    def emit(self, event_name, *args, **kwargs):
        """Dispara todos os callbacks registrados para o evento"""
        for callback in self.listeners[event_name]:
            callback(*args, **kwargs)
