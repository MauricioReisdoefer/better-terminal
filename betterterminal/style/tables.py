class BetterTable:
    """
    Exibe uma tabela simples com bordas no estilo BetterMenu.

    Args:
        headers (list[str]): Títulos das colunas.
        rows (list[list[str]]): Conteúdo da tabela.
    """

    def __init__(self, headers: list[str], rows: list[list[str]]):
        self.headers = headers
        self.rows = rows

    def show(self):
        from betterterminal import clear
        clear()
        col_widths = [len(h) for h in self.headers]
        for row in self.rows:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))

        def format_row(row):
            return "│ " + " │ ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)) + " │"

        print("┌" + "┬".join("─" * (w + 2) for w in col_widths) + "┐")
        print(format_row(self.headers))
        print("├" + "┼".join("─" * (w + 2) for w in col_widths) + "┤")
        
        for row in self.rows:
            print(format_row(row))

        print("└" + "┴".join("─" * (w + 2) for w in col_widths) + "┘")
