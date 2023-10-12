'''
Mencari y melalui L.Y = B
'''
def solveLYB(n, L, B):
    Y = [0] * n  # Inisialisasi vektor Y dengan nol

    for i in range(n):
        S = 0
        for j in range(i):
            S += L[i][j] * Y[j]

        Y[i] = (B[i] - S) / L[i][i]

    return Y

# Meminta input dari pengguna
n = int(input("Masukkan ordo matriks (n): "))

# Meminta input untuk matriks segitiga bawah L
print("Masukkan elemen-elemen matriks segitiga bawah L:")
L = []
for i in range(n):
    row = []
    for j in range(n):
        if j <= i:
            elem = float(input(f"L[{i+1},{j+1}]: "))
            row.append(elem)
        else:
            row.append(0)
    L.append(row)

# Meminta input untuk vektor hasil B
print("Masukkan elemen-elemen vektor hasil B:")
B = []
for i in range(n):
    elem = float(input(f"B[{i+1}]: "))
    B.append(elem)

solusi_Y = solveLYB(n, L, B)
print("Solusi Y =", solusi_Y)

'''
n = 3  # Ordo matriks
L = [[1, 0, 0], #baris 1 kolom 1
     [2, 1, 0], #baris 2 kolom 1, baris 2 olom 2
     [-1, 3, 1]]  # baris 3 kolom 1, baris 3 kolom2, baris 3 kolom 3
B = [1, 3, 7]  # Vektor hasil B
'''