# ПЕЧАТЬ КВАДРАТОВ ЧИСЕЛ:

# L=[]
# for i in range(0,10):
#     L.append(i**2)
#     print(L)

# ОПРЕДЕЛИТЕЛЬ МАТРИЦЫ:
import copy

L=[[1,2,3],
   [4,5,6],
   [7,8,9]]

n=len(L) # кол-во строк и соотв-но размерность
d=0

def foo(M):
    d2=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return d2

for i in range (0,n):
    M = copy.deepcopy(L)
    M.pop(0)
    M[0].pop(i)
    M[1].pop(i)
    d2=foo(M)
    d=d+(-1)**i*L[0][i]*d2

print('det =',d)

# ddd=L[0][0]*(L[1][1]*L[2][2]-L[1][2]*L[2][1])-L[0][1]*( L[1][0]*L[2][2]-L[1][2]*L[2][0] )+L[0][2]*(L[1][0]*L[2][1]-L[1][1]*L[2][0])
# print('ddd=',ddd)