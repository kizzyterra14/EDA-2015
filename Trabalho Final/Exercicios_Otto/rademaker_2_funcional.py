lst = [1201,1308,1308,1201,1403,1308]

equivalenceClasses ={}
lst_pares = []

pare = len(lst) + 1
teste_impar = len(lst) % 2 != 0

if teste_impar:
    pare = len(lst)

cont = 1
while cont != pare:
    lst_pares.append((lst[cont - 1],lst[cont]))
    cont += 2

if teste_impar:
    lst_pares.append((lst[len(lst) - 1], None))

def compara(valor1, valor2):
    #if valor1[0] == valor2[0] or valor1[0] == valor2[1]:
    if valor1 == valor2:
        return(True)
    else:
        return(False)

def testa_igual(lista):
    if lista[0] == lista[1]:
        return(lista[0])
    elif lista[0] is None:
        return(lista[1])
    elif lista[1] is None:
        return(lista[0])

def testa_dif(lista):
    if lista[0] != lista[1]:
        return((lista[0],lista[1]))

def contagem(restante, deletado):
    repeticoes = 0
    restante_lista = []
    deletado_lista = []
    #necessario transformas as listas que estavam em tuplas em apenas listas, para manter linearidade.
    for valor_tupla in restante:
        restante_lista.append(valor_tupla[0])
    for valor_tupla in deletado:
        deletado_lista.extend([valor_tupla[0],valor_tupla[1]])
    for valor in restante_lista:
        cont = 0
        if valor is None:
            next
        while cont != len(deletado_lista):
            if compara(valor,deletado_lista[cont]) is True:
                repeticoes += 1
                deletado_lista.remove(deletado_lista[cont])
                cont -= 1
            cont += 1
    return(repeticoes)

def teste(lista, parametro):
    lista_restante = []
    lista_delete = []
    for valor_igual in filter(testa_igual,lista):
        lista_restante.append(valor_igual)
    for valor_dif in filter(testa_dif, lista):
        lista_delete.append(valor_dif)
    n_repeticoes = contagem(lista_restante, lista_delete)
    if n_repeticoes > parametro:
        return(True, n_repeticoes)
    else:
        return(False, n_repeticoes)


if __name__ == "__main__":
    print(teste(lst_pares, 0))
