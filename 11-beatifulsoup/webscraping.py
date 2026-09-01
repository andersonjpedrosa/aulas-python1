# requisição
import requests

# biblioteca que transforma em objeto Python
from bs4 import BeautifulSoup

pagina = requests.get("https://quotes.toscrape.com/") 

dados_pagina = BeautifulSoup(pagina.text, "html.parser") #pega só os texto em html

#(print(dados_pagina.prettify())) #.prettify é de forma organizada

#todas_frases = dados_pagina.find_all("div", class_="quote")

#for div in todas_frases:
    #print(div)

todas_frases_filtradas = dados_pagina.find_all("span", itemprop="text")

for span in todas_frases_filtradas:
    print(span.text)