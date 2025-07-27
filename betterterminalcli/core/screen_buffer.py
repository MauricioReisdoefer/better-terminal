import sys
import time
import os
class ScreenBuffer():
    """
    A Tela Principal do Terminal, vai cuidar de toda a renderização dinâmica de caracteres.
    
    args:
        width (int) = Largura da Tela
        height (int) = Altura da Tela
        fill (str) = Representa espaço Vazio
    """
    def __init__(self, width:int = 70, height:int = 30, fill=" "):
        self.width = width
        self.height = height
        self.fill = fill
        
        # Define a Matriz Principal (Screen / Terminal)
        self.screen = [[self.fill for pixel in range(width)] for pixel in range(height)]
    
    @staticmethod
    def os_clearterminal():
        """
        Limpa a tela do terminal conforme o sistema operacional.
        """
        if os.name == 'nt': 
            os.system('cls')
        else:  
            os.system('clear')
    
    def clear(self):
        """
        Limpa a tela do terminal, mas sem renderizar.
        """
        for y in range(self.height):
            for x in range(self.width):
                self.screen[y][x] = self.fill
                
    def draw(self, x:int, y:int, text:str):
        """
        Desenha um texto na tela, sem renderizar.
        
        args:
            x (int) = Posição Horizontal do Primeiro Caractere do Texto
            y (int) = Posição Vertical do Primeiro Caractere do Texto
            text (str) = Texto para ser Desenhado na Tela
        
        IMPORTANTE: Caso o texto passe da largura ou altura máxima, ele NÃO SERÁ RENDERIZADO.
        """
        for i, char in enumerate(text):
            if 0 <= x+i < self.width and 0 <= y < self.height:
                self.screen[y][x+i] = char
    
    def render(self, draw_border: bool = True):
        """
        Renderiza a tela no terminal.
        Se draw_border=True, desenha uma borda bonita na visualização.
        """
        sys.stdout.write("\033[H")

        if draw_border:
            sys.stdout.write("┌" + "─" * self.width + "┐\n")
            for row in self.screen:
                sys.stdout.write("│" + "".join(row) + "│\n")
            sys.stdout.write("└" + "─" * self.width + "┘")
        else:
            sys.stdout.write("\n".join("".join(row) for row in self.screen))

        sys.stdout.flush()

        
    def draw_matrix(self, x:int, y:int, matrix:list[list[str]]):
        """
        Desenha uma matriz 2D na tela na posição (x,y).
        """
        for dy, row in enumerate(matrix):
            for dx, char in enumerate(row):
                absolutex, absolutey = x + dx, y + dy
                if 0 <= absolutex < self.width and 0 <= absolutey < self.height:
                    self.screen[absolutey][absolutex] = char
                