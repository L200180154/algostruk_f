#No3

def temp(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cari(A, B, C):
    posisiTerkecil = B
    for i in range(B+1, C):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def test1(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                temp(A,j,j+1)

def test2(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cari(A, i, n)
        if indexKecil != i:
            temp(A, i, indexKecil)

def test3(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

p = detak();test1(u_bub);t=detak();print("Bubble    : %g detik"%(t-p));
p = detak();test2(u_sel);t=detak();print("Selection : %g detik"%(t-p));
p = detak();test3(u_ins);t=detak();print("Insertion : %g detik"%(t-p));
