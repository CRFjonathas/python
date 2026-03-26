from PIL import Image
import numpy as np

def main():
    # Carregar a imagem original
    img = Image.open("simple_icon.png")

    # Converter a imagem em dados binarios
    img_data = np.array(img)
    binary_data = img_data.tobytes()

    print("\n", img_data.shape,"\n")

    # Salvar os dados binarios em um arquivo
    with open("original_img.bin", "wb") as file:
        file.write(binary_data)

    # Copiar o arquivo binário
    with open("original_img.bin", "rb") as original_file:
        data = original_file.read()

    with open("copy_img.bin", "wb") as copy_file:
        copy_file.write(data)

    # Manipulação dos dados do arquivo binario copia 
    # Exemplo: inverter os bytes
    with open("copy_img.bin", "rb") as file:
        data = bytearray(file.read())
