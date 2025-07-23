class BetterMenu():       
    """
    Cria um menu com navegação por setas e seleção com Enter.

    Args:
        title (str): Título exibido no topo do menu.
        options (list[str]): Lista de strings representando cada opção.
        cursor (str): Símbolo que indica a opção selecionada (default: ">").
    """
    
    def __init__(self, title:str="No Title", options:list[str]=["No Options"], cursor:str=">"):
        self.title = title
        self.options = options
        self.cursor = cursor
    
    def show_menu(self):
        import readchar
        from betterterminal import clear
        indice = 0

        while True:
            clear()

            linhas = [self.title, ""] 
            for i, opcao in enumerate(self.options):
                prefixo = f"{self.cursor} " if i == indice else " " * (len(self.cursor) + 1)
                linhas.append(f"{prefixo}{opcao}")

            largura = max(len(linha) for linha in linhas) + 4 

            print("┌" + "─" * (largura - 2) + "┐")

            for i, linha in enumerate(linhas):
                if i == 0:
                    print("│ " + linha.center(largura - 4) + " │")
                else:
                    print("│ " + linha.ljust(largura - 4) + " │")

            print("└" + "─" * (largura - 2) + "┘")

            tecla = readchar.readkey()
            if tecla == readchar.key.UP:
                indice = (indice - 1) % len(self.options)
            elif tecla == readchar.key.DOWN:
                indice = (indice + 1) % len(self.options)
            elif tecla == readchar.key.ENTER:
                return indice
