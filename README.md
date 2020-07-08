# Desafio-CM
Desafio para a vaga de estágio da CM tecnologia.

## Teste-1
Dois problemas são abordados:

## 1)A soma dos algarismos de um numero.
```
ex) 123 = 6
Para resolver este problema usei a divisao e o resto por 10.
ex) 123/10 = 12 (pegando a parte inteira)
	123%10 = 3
	repetindo o processo..
	12/10 = 1
	12%10 = 2
	
	Dessa forma eu consigo pegar os algarismos
	armazena-los e entao soma-los.
	
	E usei recursão para otimizar o processo.
```
	
## 2)A multiplicação de uma String.
```
ex) 12 * 3 = 121212
Para resolver esse problema usando python é facil.
Basta multiplicar a string pelo inteiro, que o python
entende e nos retorna o resultado esperado.
```

## Para executar: 
```
	python teste-1.py
	Uma vez executado escolha o problema atraves do menu.
```
	
## Teste-2 - Extração de dados
Usar a técnica de webscraping para extrair informações do portal http://quotes.toscrape.com/ e armazenar em um arquivo JSON.

## Pré-requisitos

* Python 3.x
* Geckodriver
* Google Chrome
* Algumas bibliotecas do python

## Instalação

## Instale as seguintes bibliotecas com o pip
	
* **requests2** - É útil
* **pandas** - Biblioteca para trabalhar com dados em python;
* **lxml** - Biblioteca para processar XML e HTML;
* **beautfulsoup4** - Biblioteca para extrair de fato dados de HTML e XML;
* **selenium** - Voce vai usar para acessar e clicar no site.
	 
## Instale o Geckodriver com o pip e o driver para chrome
```	 
pip install webdrivermanager
webdrivermanager chrome --linkpath /usr/local/bin
```

## Execute o codigo
```
python webscraping.py
```


	