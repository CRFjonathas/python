def teste(b):
    global a  
    a = 8
    b += 4
    c = 2
    print(f'A denrtro vale {a}')
    print(f'B denrtro vale {b}')
    print(f'C denrtro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')