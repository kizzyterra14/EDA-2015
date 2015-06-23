import random
def quadratic(L):
    sizeL = len(L)
    if sizeL == 0:
        return L
    max_sum = L[0]
    max_subsequence = L[:1]
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
    max_subsequence = L[:1]
    for j in range(1, sizeL):
        for i in range(j): 
            current_sum = 0
            for k in range(i,j):
                current_sum += L[k]
            if current_sum > max_sum:
                max_sum = current_sum
                max_subsequence = L[i:j]
    return max_subsequence

if __name__ == '__main__':
    print cubic([random.randrange(-100000, 100000, 1) for i in xrange(10000)])