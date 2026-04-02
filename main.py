# DP para soma de minkowski geral

def MinkowskiSum(matriz, k):
    sum = 0
    
    for i in range(0, k):
        sum = sum + max(matriz[i])

    prev = [False] * (sum + 1)
    curr = [False] * (sum + 1)
    aux = [False] * (sum + 1)
    
    for i in matriz[0]:
        prev[i] = True
            
    for z in range(1, k):
        for i in range(0, len(matriz[z])):
            for j in range(1, sum + 1):
                if prev[j] == True:
                    curr[j+matriz[z][i]] = True
        prev = curr.copy()
        curr = aux.copy()
    return prev


if __name__ == "__main__":
    #Coleção dos fatores dessa soma de minkowski
    D = [
        [1,5],
        [1,6,9],
        [1,5,11],
        [3]
    ]
    
    M = []
    for v in D:
        M.append(v)
    k = len(M)
    
    print('Matriz = {}'.format(M))
    res = MinkowskiSum(M, k)
    for i in range(len(res)):
        if res[i] == True:
            print('{}'.format(i))
            
# Complexidade da op: O(sum*k*n)
# Espaco ocupado (dp): O(sum)
# Sem recursao