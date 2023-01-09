from selenium import webdriver as opcao
from selenium.webdriver.common.by import By
import pyautogui as tempo

navegador = opcao.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

tempo.sleep(3)
navegador.find_element(By.NAME,"endereco").send_keys("23045460")
tempo.sleep(3)

navegador.find_element(By.NAME,"btn_pesquisar").click()
tempo.sleep(3)


tabela = navegador.find_element(By.XPATH,'//*[@id="resultado-DNEC"]')
for i in tabela.find_elements(By.TAG_NAME,'tr'):
    endereco = ''
    for x in i.find_elements(By.TAG_NAME,'td'):
        endereco = endereco + ';' + x.text
        
print (endereco)
        
