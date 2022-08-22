#!/usr/bin/env python
# coding: utf-8

# # Automação Web e Busca de Informações com Python
# 
# #### Desafio: 
# 
# Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:
# - Dólar
# - Euro
# - Ouro
# 
# Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.
# 
# Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing
# 
# Para isso, vamos criar uma automação web:
# 
# - Usaremos o selenium
# - Importante: baixar o webdriver

# In[ ]:


get_ipython().system('pip install selenium')


# In[21]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Pegar cotação do dólar
navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/')
navegador.find_element(
    'xpath',
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
).send_keys('cotacao dolar')

navegador.find_element(
    'xpath',
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
).submit()

cotacao_dolar = navegador.find_element(
    'xpath',
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).get_attribute('data-value')

# Pegar a cotação do euro
navegador.get('https://www.google.com.br/')
navegador.find_element(
    'xpath',
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
).send_keys('cotacao euro')

navegador.find_element(
    'xpath',
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
).submit()

cotacao_euro = navegador.find_element(
    'xpath',
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).get_attribute('data-value')

# Pegar a cotação do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element(
    'xpath',
    '//*[@id="comercial"]'
).get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')
print(cotacao_ouro)

navegador.quit()


# ### Agora vamos atualiza a nossa base de preços com as novas cotações

# - Importando a base de dados

# In[22]:


import pandas as pd

tabela = pd.read_excel('Produtos.xlsx')

display(tabela)


# - Atualizando os preços e o cálculo do Preço Final

# In[ ]:





# ### Agora vamos exportar a nova base de preços atualizada

# In[ ]:




