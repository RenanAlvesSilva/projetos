from http import server 
from multiprocessing.managers import Server
from sqlite3 import connect
from tkinter import INSERT
from PyQt5 import uic,QtWidgets
import mysql.connector





#banco = mysql.connector.connect(
   
#user = "",
#passwd = "",
#database = ""
#)


def cadastrar():
    tipo = tela.lineEdit.text()
    print("TIPO: ",tipo)
    Tamanho_Produto = tela.lineEdit_2.text()
    print("Tamanho_Produdo: ",Tamanho_Produto)
    Quantidade_Produto = tela.lineEdit_3.text()
    print("Quantidade_Produto: ",Quantidade_Produto)
    
    
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO pessoas (tipo, tamanho_produto, quantidade_produto ) VALUES (%s, %s, %s)"
    dados = (str(tipo), str(Tamanho_Produto), str(Quantidade_Produto))
    cursor.execute(comando_SQL, dados)
    banco.commit()
    tela.lineEdit.setText("")
    tela.lineEdit_2.setText("")
    tela.lineEdit_3.setText("")
    
    
    
def segunda_tela2():
    segunda_tela.show()  
    
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM pessoas"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    
    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(4)
    
    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            segunda_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem (str (dados_lidos [i][j])))
    

app = QtWidgets.QApplication([])
tela = uic.loadUi("r2p2.ui")
segunda_tela = uic.loadUi("tela2.ui")


tela.cadastrar.clicked.connect(cadastrar)
tela.pushButton.clicked.connect(segunda_tela2)

tela.show()
app.exec()

""" CREATE TABLE pessoas (id INT NOT NULL AUTO_INCREMENT,
NOME VARCHAR(100),
ANIVERSARIO INT(20),
ENDERECO VARCHAR(200),
SEXO VARCHAR(15),
TELEFONE VARCHAR(35),
CPF INT(35),
TIPO_CADASTRO VARCHAR(20),
PRIMARY KEY(id));

INSERT INTO pessoas (id, nome, aniversario, endereco, sexo, telefone, cpf, tipo_cadastro) 
VALUES (1,"Renan", 1602995, "Sarjento Jaime", "MASCULINO", 966080941, 14651635733, "CADASTRO"); """