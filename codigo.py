# Passo a passo do projeto


# Passo 1 - Entrar no sistema da empresa:
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# instalar bibliotecas em python:
# pip install pyautogui - RPA - automação bot
# apos instalação segue codigo:

import pyautogui
import time
# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey
# scroll (rolar pagina para cima e cadastrar novo produto) -> pyautogui.scroll
pyautogui.PAUSE = 1 #serve para pausar 1 segundo a cada comando para ver o que esta acontecendo durante a construcao do codigo pois e muito rapido
# apertar a tecla do windows (command + barra de espaça)
pyautogui.press("win")
#digita o nome do programa (chrome)
pyautogui.write("chrome")
# aperta enter
pyautogui.press("enter")
# digitar o link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
# apertar enter
pyautogui.press("enter")

#espera 5 segundos
time.sleep(5)

# Passo 2 - fazer login
pyautogui.click(x=1894, y=944)

# digitar e-mail
pyautogui.write("caiomatsuidev@outlook.com")

# passar para o campo da senha
pyautogui.press("tab")

# digitar senha
pyautogui.write("minhasenha")

# clicar no botao logar
pyautogui.click(x=2035, y=1101)
time.sleep(3)

# Passo 3 - Importar a base de dados
#pip install pandas numpy openpyxl
import pandas as pd 

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: #.index todas as linhas da tabela, . columns sao todas as colunas da tabela!
    # Passo 4 - Cadastrar um produto
    # primero cadastrar um produto manualmente
    pyautogui.click(x=1893, y=835)
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): #verifica se o valor esta vazio, ex: NaN   1219.95 5.0     25.0    11.0
        pyautogui.write(obs)
    # enviar produto
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(1000)

# Passo 5 - Repetir isso até acabar a base de dados

# Isso tudo citado acima é a chamada Lógica de programação!


