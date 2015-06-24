import Levenshtein

#Exemplo de como o dataset sera estruturado para fazermos a analise desejada.
lst = [("UFRJ","UERJ"), ("EMAP","EBAPE"), ("PUC Rio","PUC-MG"), ("UFF","FGV"), ("EBEF","EPGE"), ("UFRRJ","UFMG")]

def testa_igual(valor):
    distancia_str = Levenshtein.distance(valor[0],valor[1])
    if distancia_str <= 2:
    	print valor
        return(1)
    else:
        return(0)

def contagem(lista):
    cont = 0
    for lst in lista:
        cont += testa_igual(lst)
    return cont 

if __name__ == "__main__":
	print contagem(lst)
   