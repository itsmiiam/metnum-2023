'''
Mencari LU
'''
import numpy as np

def LU_Factorization(A, n):
    L = np.zeros((n, n), dtype=float)
    U = np.zeros((n, n), dtype=float)

    for i in range(n):
        L[i, i] = 1  # Isi elemen diagonal utama L dengan 1
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

    return L, U

# Meminta input dari pengguna
n = int(input("Masukkan ordo matriks (n): "))

# Meminta input untuk matriks koefisien A
print("Masukkan elemen-elemen matriks koefisien A:")
A = np.zeros((n, n), dtype=float)
for i in range(n):
    for j in range(n):
        elem = float(input(f"A[{i+1},{j+1}]: "))
        A[i, j] = elem

L, U = LU_Factorization(A, n)
print("Matriks segitiga bawah L:")
print(L)
print("Matriks segitiga atas U:")
print(U)

'''
Masukkan ordo matriks (n): 3
Masukkan elemen-elemen matriks koefisien A:
A[1,1]: 2
A[1,2]: 3
A[1,3]: -1
A[2,1]: 4
A[2,2]: 7
A[2,3]: 2
A[3,1]: -2
A[3,2]: 4
A[3,3]: 3

Matriks segitiga bawah L:
[[ 1.  0.  0.]
 [ 2.  1.  0.]
 [-1.  2.  1.]]

Matriks segitiga atas U:
[[ 2.  3. -1.]
 [ 0.  1.  4.]
 [ 0.  0.  5.]]

'''