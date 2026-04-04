from classes.Controle import ControleRemoto
from rich import print

c = ControleRemoto()
while True:
    c.mostrar_tv()
    comando = str(input(f" < CH{c.canal_atual} >   - VOL{c.volume_atual} + "))
    match comando:
        case '0':
            break
        case '@':
            c.liga_desliga()
        case '-':
            c.volume_menos()
        case '+':
            c.volume_mais()
        case '<':
            c.canal_menos()
        case '>':
            c.canal_mais()
    print("\n" *10)