import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Pegando o conteudo a partir da URL

url = "http://quotes.toscrape.com"

option = Options()
option.headless = True

driver = webdriver.Chrome(options=option, executable_path=r"C:\usr\local\bin\chromedriver.exe")

driver.get(url)
driver.implicitly_wait(10)  # in seconds

element = driver.find_element_by_xpath("//div[@class='container']/div[@class='row']/div[@class='col-md-8']")

html_content = element.get_attribute('outerHTML')

#Parsear o conteudo HTML com beautifulSoup

soup = BeautifulSoup(html_content, 'html.parser')
elementos = soup.findAll(class_="quote")

#Colocando tudo em uma lista e parseando mais um pouco
lista_elementos = [] #aqui vou salvar uma lista de listas=[frase,autor,tags]
for e in elementos:
    list_aux = []
    soup_aux = BeautifulSoup(str(e), 'html.parser')

    #Pegando a frase
    text = soup_aux.find(name='span', class_='text')
    text= text.contents[0]
    list_aux.append(text)

    #Pegando o autor
    autores = soup_aux.find(class_='author')
    autores = autores.contents[0]
    list_aux.append(autores)

    #Pegando as tags e colocando em uma string
    tags = soup_aux.findAll("a", class_='tag')
    list_tags = [t.contents[0] for t in tags]
    txt = ""
    for t in list_tags:
        txt += t + " "
    list_aux.append(txt)

    #juntando tudo
    lista_elementos.append(list_aux)

#Colocando tudo num DataFrame usando a Lista
df = pd.DataFrame(data=lista_elementos, columns=['Frase','Autor','Tags'])
print(df)

#Exportanto
df.to_json(r'C:\Users\Jean_Lucas\prog\python\web_scraping\frases.json',orient='split')
#df.to_csv(r'C:\Users\Jean_Lucas\prog\python\web_scraping\frases.csv', sep=";")


driver.quit()