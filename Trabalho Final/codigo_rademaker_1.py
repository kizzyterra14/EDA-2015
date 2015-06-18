#Esse codigo tem o objetivo de criar uma schedule do exercico X da Eva Tardos
lista = [(24,5),(31,9),(57,22),(39,56),(5,1),(82,43)]

#Funcao auxiliar criada para selecionar elementos da tupla que serao comparados
def compare(a, b):
    return a[1] >= b[1]
#Funcao merge que faz a operacao de sort ao concatenar o maior elemento
#com os demais elementos da lista
def merge(lista_rst, lista_nd):
    if len(lista_rst) is 0:
        return(lista_nd)
    elif len(lista_nd) is 0:
        return(lista_rst)
    else:
        #Modificacao para iterar entre tuplas e ordenar em ordem decrescente
        #dos valores dos jobs dos PCs
        if compare(lista_rst[0], lista_nd[0]):
            temp = [lista_rst[0]]
            temp.extend(merge(lista_rst[1:],lista_nd))
            return(temp)
        else:
            temp = [lista_nd[0]]
            temp.extend(merge(lista_rst,lista_nd[1:]))
            return(temp)

def mergesort_inverse(lista):
    if len(lista) <= 1:
        return(lista)
    else:
        med = len(lista) // 2
        result = merge(mergesort_inverse(lista[:med]),mergesort_inverse(lista[med:]))
        return(result)

#jobs e uma lista de tuplas, tendo o job do supercomputador como primeiro elemento
#e o job do PC como segundo
def schedule(jobs):
    #deve-se ordenar jobs de maneira decrescente nos tempos de trabalho dos PCs
    return(mergesort_inverse(jobs))


if __name__ == "__main__":
    print(mergesort_inverse(lista))
