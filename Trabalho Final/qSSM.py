import random
def quadratic(L):
    sizeL = len(L)
    if sizeL == 0:
        return L
    max_sum = L[0]
    max_subsequence = []

    for i in range(sizeL):          
        max_subsequence.append(L[i]) 
    for j in range(sizeL):
        current_sum = 0
        for i in range(j, sizeL):
            current_sum += L[i]
            if current_sum > max_sum:
                max_sum = current_sum
                max_subsequence = L[j:i+1]
    return max_subsequence

def cubic(L):
    sizeL = len(L)
    if sizeL == 0:
        return L
    max_sum = L[0]
    max_subsequence = []
    for i in range(sizeL):          
        max_subsequence.append(L[i]) 

    for j in range(1, sizeL):
        for i in range(j): 
            current_sum = 0
            for k in range(i,j):
                current_sum += L[k]
            if current_sum > max_sum:
                max_sum = current_sum
                max_subsequence = L[i:j]
    return max_subsequence

def algoritmo_cubico(X):
    max_ate_agora = 0.0
    N = len(X)
    for L in range(1, N + 1):
        for U in range(L, N + 1):
            soma = 0.0
            for I in range(L, U + 1):
                soma = soma + X[I - 1]
            max_ate_agora = max(max_ate_agora, soma)
    return max_ate_agora


if __name__ == '__main__':
    print cubic([random.randrange(-100000, 100000, 1) for i in xrange(1000)])