def main():
    print("Digite seu texto.\nDigite 'sair' para terminiar e salvar o arquivo.\n")
    textos = []
    
    while True:
        entrada = input("> ")
        if entrada.lower() == "sair":
            break
        textos.append(entrada)

    with open("/workspaces/python/Faculdade/RAD/Manipulação-de-Dados-em-Arquivos/Funções-de-manipulação-de-arquivos/Manipulando-arquivo-texto-em-Python/meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
        for texto in textos:
            arquivo.write(texto + "\n")

    print("Arquivo original criado. Agora vamos manipular os dados.")
    dados_modificados = []
    with open("/workspaces/python/Faculdade/RAD/Manipulação-de-Dados-em-Arquivos/Funções-de-manipulação-de-arquivos/Manipulando-arquivo-texto-em-Python/meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados_modificados.append(linha.strip().upper())

    with open("/workspaces/python/Faculdade/RAD/Manipulação-de-Dados-em-Arquivos/Funções-de-manipulação-de-arquivos/Manipulando-arquivo-texto-em-Python/meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + "\n")
    

    print("O arquivo foi sobrescrito com os dados modificados.")

if __name__ == "__main__":
    main()