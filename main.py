# DP para soma de minkowski geral

def MinkowskiSum(matriz, k):
    sum = 0
    
    for i in range(0, k):
        sum = sum + max(matriz[i])

    prev = [False] * (sum + 1)
    curr = [False] * (sum + 1)
    aux = [False] * (sum + 1)
    
    for i in range(sum + 1):
        if i in matriz[0]:
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
    V1 = [1,5]
    V2 = [1,6,9]
    V3 = [3]
    M = []
    M.append(V1)
    M.append(V2)
    M.append(V3)
    k = len(M)
    print('Matriz = {}'.format(M))
    res = MinkowskiSum(M, k)
    for i in range(len(res)):
        if res[i] == True:
            print('{}'.format(i))
            
# Complexidade da op: O(sum*k*k*n)
# Espaco ocupado (dp): O(sum*k)
# Sem recursao