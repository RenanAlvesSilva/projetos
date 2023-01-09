from selenium import webdriver as opcao
from selenium.webdriver.common.by import By
import pandas as pd

navegador = opcao.Chrome()

navegador.get('https://pt.wikipedia.org/wiki/Lista_dos_canais_com_mais_inscritos_do_YouTube')

elemento = navegador.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]')

linhas = elemento.find_elements(By.TAG_NAME, 'tbody')
colunas = elemento.find_elements(By.TAG_NAME, 'tr')
dataframelista = []
linha = 1

for i in colunas:
    print(i.text)
    dataframelista.append(i.text)
    linha += linha
    
arquivo = pd.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter')
arquivo.save()

dataframe = pd.DataFrame(dataframelista, columns=[['coluna_dados']])
arquivo = pd.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter')
dataframe.to_excel(arquivo, sheet_name='sheet1', index= True)

arquivo.save()