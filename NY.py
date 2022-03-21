#Importando Bibliotecas
import requests
from bs4 import BeautifulSoup
from lxml import html

requisiçao = requests.get ('https://www.nytimes.com/') # Site que iremos minerar
soup = BeautifulSoup (requisiçao.content,'html.parser') #Método que permiti a lib acessar o HMTL

print ('.:: Iniciando Busca ::.') 

tituloNoticia = soup.find_all ('h2',{'class':'css-1qwxefa esl82me0'}) #XPATH do elmento da página
corpoNoticia = soup.find_all ('ul',{'class':'css-1rrs2s3 e1n8kpyg1'}) #XPATH do elmento da página

for i in tituloNoticia: # Laço de repetiçao que pegará o titulo e corpo da noticia
    print ('Titulo Noticia: {}'.format(i.text))
    for j in corpoNoticia:
        print ('Noticia: {}'.format(j.text))

print ('.:: Fim das Buscas ::. ')