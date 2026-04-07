# DP para soma de minkowski geral

def MinkowskiSum(matriz):
    bigst = 0
    k = len(matriz)
    
    for i in range(0, k):
        bigst = bigst + max(matriz[i])

    prev = [False] * (bigst + 1)
    curr = [False] * (bigst + 1)
    aux = [False] * (bigst + 1)
    
    for i in matriz[0]:
        prev[i] = True
            
    for z in range(1, k):
        for i in range(0, len(matriz[z])):
            for j in range(1, bigst + 1):
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
        [3],
        [1,2,3,27,81]
    ]
    
    M = []
    for v in D:
        M.append(v)
    
    print('Matriz = {}'.format(M))
    res = MinkowskiSum(M)
    for i in range(len(res)):
        if res[i] == True:
            print('{}'.format(i))
            
# Complexidade da op: O(bigst*k*n)
# Espaco ocupado (dp): O(bigst)
# Sem recursao