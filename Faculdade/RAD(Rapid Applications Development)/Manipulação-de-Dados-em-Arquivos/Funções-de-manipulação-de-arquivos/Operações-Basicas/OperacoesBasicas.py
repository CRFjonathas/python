import os

arquivo1 = open("teste.txt", "w", encoding="utf-8")
print(os.path.abspath(arquivo1.name))

arquivo1.write("Olà, mundo!")

print(arquivo1)
arquivo1.close
