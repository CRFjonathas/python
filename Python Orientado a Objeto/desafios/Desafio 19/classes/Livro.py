from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        
        print(f"[blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} paginas[/] no total. Você agora está na [yellow]página 1[/][/]")

    def avancar_pagina(self, pag):
        
        for i in range(pag):
            self.pagina_atual +=1
            print(f"Pág{self.pagina_atual} ->", end=" ")
            sleep(0.3)
            
            if self.pagina_atual >= self.paginas:
                pag = i + 1
                break

        print(f"[blue]Você avançou {pag} páginas e agora está na [green]página {self.pagina_atual}[/][/]")

        if self.pagina_atual == self.paginas:
            print(f"[red]Você chegou ao final do livro '{self.titulo}'[/]")
               
