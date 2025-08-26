import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.flamengo.com.br/')
except urllib.error.URLError:
    print('O site do Flamengo não está acessivel no momento.')
else:
    print('Consegui acessar o site do Flamengo com sucesso.')