from rich import print
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1
        
        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.total_paginas} paginas[/] no total. Você agora está na [yellow]página {self.pagina_atual}[/][/]")

    def avancar_pagina(self, qtd = 1):
        count = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward:", end=' ')
                count += 1
                time.sleep(0.2)
                
        print(f"[blue]Você avançou {count} páginas e agora está na [green]página {self.pagina_atual}[/][/]")

        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")

    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False
               
