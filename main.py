from openpyxl import Workbook
from datetime import date
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
from openpyxl.chart import BarChart, Reference, Series
from openpyxl.chart import (LineChart,Reference)

# acao = input("Qual o codigo da Ação que você quer processar? ").upper()
acao = "BIDI4"

with open(f'./dados/{acao}.txt','r') as arquivo_cotacao:
    linhas = arquivo_cotacao.readlines()
    linhas = [linha.replace("\n", "").split(";") for linha in linhas]

workbook = Workbook()
planilha_ativa = workbook.active
planilha_ativa.title = "Dados"

planilha_ativa.append(["DATA", "COTAÇÃO", "BANDA INFERIOR", "BANDA SUPERIOR"])

indice = 2

for linha in linhas:
    # Data
    ano_mes_dia = linha[0].split(" ")[0]
    data = date(
        year=int(ano_mes_dia.split("-")[0]),
        month=int(ano_mes_dia.split("-")[1]),
        day=int(ano_mes_dia.split("-")[2])
    )
    # COTAÇÃO
    cotacao = float(linha[1])

    #Atualiza as células da Planilha Ativa do Excel
    planilha_ativa[f'A{indice}'] = data
    planilha_ativa[f'B{indice}'] = cotacao
    planilha_ativa[f'C{indice}'] = f'=AVERAGE(B{indice}:B{indice + 19}) - 2*STDEV(B{indice} + B{indice + 19})'
    planilha_ativa[f'D{indice}'] = f'=AVERAGE(B{indice}:B{indice + 19}) + 2*STDEV(B{indice} + B{indice + 19})'

    indice += 1

planilha_grafico = workbook.create_sheet("Grafico")
workbook.active = planilha_grafico

#Mesclagem de celulas para criação do cabeçalho do gráfico
planilha_grafico.merge_cells("A1:T2")
cabecalho = planilha_grafico["A1"]
cabecalho.font = Font(b=True, sz=18, color="FFFFFF")
cabecalho.fill = PatternFill("solid", fgColor="2a6637")
cabecalho.alignment = Alignment(vertical="center", horizontal="center")
cabecalho.value = "Histórico de Cotações"

grafico = LineChart()
grafico.width = 33.87
grafico.height = 14.82
grafico.title = "Histórico de Cotações"
grafico.x_axis.tittle = "Data da Cotação"
grafico.y_axis.title = "Valor da Cotação"

referencia_cotacoes = Reference(planilha_ativa, min_col=2, min_row=2, max_col=4, max_row=indice)
referencia_datas = Reference(planilha_ativa, min_col=1, min_row=2, max_col=1, max_row=indice)
grafico.add_data(referencia_cotacoes)
grafico.set_categories(referencia_datas)

planilha_grafico.add_chart(grafico, "A3")

workbook.save("./saida/Planilha.xlsx")
