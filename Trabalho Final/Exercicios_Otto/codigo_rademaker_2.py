
#Vamos utilizar o exercicio 3 do capitulo 5 de divisao e conquista do livro Algorithm Design de John Kleinberg e de Eva Tardos
#como inspiracao para resolucao de um problema real com uma base de dados do setor de matematica.
#O problema consiste na comparacao de strings a fim de descobrir qual a proporcao de professores
#que se tornou pesquisador do mesmo programa que se titulou.

#Bibliotecas necessarias para importar e tratar o dataset que sera utilizado para analise
import xlrd
import re
import nltk
import Levenshtein

#Exemplo de como o dataset sera estruturado para fazermos a analise desejada.
lst = [("UFRJ","UERJ"), ("EMAP","EBAPE"), ("PUC Rio","PUC-MG"), ("UFF","FGV"), ("EBEF","EPGE"), ("UFRRJ","UFMG")]

#Importando e Limpando os dados
matematica_wb = xlrd.open_workbook("Matematica.xlsx", encoding_override = "utf8" )
matematica_ws = matematica_wb.sheet_by_index(0)
instituicao = matematica_ws.col(4)
instituicao_sigla = matematica_ws.col(3)
titulacao = matematica_ws.col(52)
titulacao_IES = []
titulacao_sigla  =[]
cont = 0
for valor in titulacao:
    valor_split = re.split("/",str(valor))
    titulacao_IES.append((str(instituicao[cont]).upper(),valor_split[0].upper()))
    cont += 1

#Lista constituida de tuplas indicando a instituicao onde o professor se titulou e onde ele trabalha
#como inlustrado no exemplo acima.
lst_tit_ies = titulacao_IES[1:]

#Funcao que fara o teste de igualdade entre as insititucoes em questao.
#Utilizamos a distancia de Levenshtein para admitir certa margem de diferenca entre as strings
#uma vez que nao existe um padrao entre elas.
def testa_igual(valor):
    distancia_str = Levenshtein.distance(valor[0],valor[1])
    if distancia_str <= 2:
        return(1)
    else:
        return(0)
#Funcao que fara a contagem de casos de igualdade, isto e, casos em que os professores se titularam
#e trabalham na mesma instituicao
def contagem(lista):
    if len(lista) is 0:
        return(0)
    if len(lista) is 1:
        return(testa_igual(lista[0]))
    else:
        med =len(lista)//2
        return(contagem(lista[:med]) + contagem(lista[med:]))

#Funcao que recebe os dados e faz a comparacao a um determinado parametro de interesse, isto e,
#para a responder a seguinte pergunta: Qual a proporcao de professores nos programas de Matematica do Brasil
#que se titularam e pesquisam no mesmo programa?
def verifica(universidades,parametro):
    if contagem(universidades) > parametro:
        return(True,contagem(universidades))
    else:
        return(False,contagem(universidades))

if __name__ == "__main__":
    print(verifica(lst_tit_ies, (2/3)*len(lst_tit_ies)))
