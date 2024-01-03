from openpyxl.drawing.image import Image
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import LineChart, Reference
from datetime import date
from openpyxl import Workbook



# acao = input("Qual o codigo da Ação que você quer processar? ").upper()
acao = "BIDI4"

leitor_acoes = LeitorAcoes(caminho_arquivo= './dados')
leitor_acoes.processa_arquivo(acao)

gerenciador = GerenciadorPlanilha()
gerenciador.adiciona_planilha("Dados")

gerenciador.adiciona_linha(["DATA", "COTAÇAO", "BANDA INFERIOR", "BANDA SUPERIOR"])

indice = 2

for linha in leitor_acoes.dados:
    # Data
    ano_mes_dia = linha[0].split(" ")[0]
    data = date(
        year=int(ano_mes_dia.split("-")[0]),
        month=int(ano_mes_dia.split("-")[1]),
        day=int(ano_mes_dia.split("-")[2])
    )
    # COTAÇÃO
    cotacao = float(linha[1])

    formula_bb_inferior = f'=AVERAGE(B{indice}:B{indice + 19}) - 2*STDEV(B{indice}:B{indice + 19})'
    formula_bb_superior = f'=AVERAGE(B{indice}:B{indice + 19}) + 2*STDEV(B{indice}:B{indice + 19})'

    #Atualiza as células da Planilha Ativa do Excel
    gerenciador.atualiza_celula(celula=f'A{indice}', dado =data)
    gerenciador.atualiza_celula(celula=f'B{indice}', dado=cotacao)
    gerenciador.atualiza_celula(celula=f'C{indice}', dado=formaula_bb_inferior)
    gerenciador.atualiza_celula(celula=f'D{indice}', dado=formaula_bb_superior)


    indice += 1

gerenciador.adiciona_planilha(titulo_planilha='Grafico')

#Mesclagem de celulas para criação do cabeçalho do gráfico
gerenciador.mescla_celulas(celula_inicio='A1', celula_fim='T2')

gerenciador.aplica_estilos(
    celula='A1',
    estilos=[
        ('font', Font(b=True, sz=18, color="FFFFFF")),
        ('alignment', Alignment(vertical="center", horizontal="center")),
        ('fill', PatternFill("solid", fgColor="2a6637")),
    ]
)


gerenciador.atualiza_celula('A1','Histórico de Cotações')

referencia_cotacoes = Rference(planilha_dados, min_col=2, min_row=2, max_col=4, max_row=indice)
referencia_datas = Reference(planilha_dados, min_col=1, min_row=2, max_col=1, max_row=indice )

gerenciador.adiciona_grafico_linha(
        celula='A3',
        comprimento=33.87,
        altura=14.82,
        titulo=f"Cotações - {acao}",
        titulo_eixo_x=referencia_cotacoes,
        titulo_eixo_y=referencia_datas,
        propriedades_grafico=[
            PropriedadeSerieGrafico(grossura=0, cor_preenchimento='0a55ab'),
            PropriedadeSerieGrafico(grossura=0, cor_preenchimento='cc3131'),
            PropriedadeSerieGrafico(grossura=0, cor_preenchimento='208031'),
        ]
)

gerenciador.salva_arquivo('./saida/PlanilhaRefatorada.xlsx')