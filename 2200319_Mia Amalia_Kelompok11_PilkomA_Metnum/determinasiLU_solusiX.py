'''
Mencari Y melalui U.X = Y
'''
import numpy as np

def solveUXY(U, Y):
    n = len(Y)  # Menentukan ordo matriks U
    X = np.zeros(n, dtype=float)  # Inisialisasi vektor X dengan nol

    for i in range(n - 1, -1, -1):
        X[i] = (Y[i] - np.dot(U[i, i + 1:], X[i + 1:])) / U[i, i]

    return X

# Meminta input dari pengguna
n = int(input("Masukkan ordo matriks (n): "))

# Meminta input untuk matriks segitiga atas U
print("Masukkan elemen-elemen matriks segitiga atas U:")
U = np.zeros((n, n), dtype=float)
for i in range(n):
    for j in range(i, n):
        elem = float(input(f"U[{i+1},{j+1}]: "))
        U[i, j] = elem

# Meminta input untuk vektor Y
print("Masukkan elemen-elemen vektor Y:")
Y = np.zeros(n, dtype=float)
for i in range(n):
    elem = float(input(f"Y[{i+1}]: "))
    Y[i] = elem

solusi_X = solveUXY(U, Y)
print("Solusi X =", solusi_X)

'''
Masukkan ordo matriks (n): 3
Masukkan elemen-elemen matriks segitiga atas U:
U[1,1]: 2
U[1,2]: 1
U[1,3]: 3
U[2,2]: 4
U[2,3]: 1
U[3,3]: 2
Masukkan elemen-elemen vektor Y:
Y[1]: 7
Y[2]: 11
Y[3]: 5
'''