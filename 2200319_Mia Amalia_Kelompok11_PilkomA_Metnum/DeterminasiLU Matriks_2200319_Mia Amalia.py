import numpy as np  # Mengimpor pustaka numpy untuk operasi matriks

def LU(A, b):
    n = len(A)  # Menentukan ukuran matriks A
    L = np.zeros((n, n))  # Membuat matriks segitiga bawah L dengan ukuran n x n

    for i in range(n):
        L[i][i] = 1  # Menginisialisasi elemen diagonal matriks L sebagai 1

    for k in range(n - 1):  # Looping untuk eliminasi Gauss
        if A[k][k] == 0:
            for s in range(n):  # Pertukaran baris jika elemen diagonal nol
                v = A[k][s]
                u = A[k + 1][s]
                A[k][s] = u
                A[k + 1][s] = v

        for j in range(k + 1, n):
            m = A[j][k] / A[k][k]  # Menghitung faktor pengali
            L[j][k] = m  # Menyimpan faktor pengali dalam matriks L
            for i in range(n):
                A[j][i] = A[j][i] - m * A[k][i]  # Mengurangkan baris ke-j dengan baris ke-k

    print('Matriks L (segitiga bawah):')
    print(L)  # Mencetak matriks segitiga bawah L

    print('Matriks U (segitiga atas):')
    print(A)  # Mencetak matriks segitiga atas U

    y = np.zeros((n, 1))  # Membuat vektor nol y

    # Menghitung solusi y dari matriks L dan vektor b menggunakan metode substitusi maju
    y[0][0] = b[0][0] / L[0][0]
    for j in range(1, n):
        S = 0
        for i in range(j):
            S = S + y[i][0] * L[j][i]
        y[j][0] = b[j][0] - S

    x = np.zeros((n, 1))  # Membuat vektor nol x

    # Menghitung solusi x dari matriks U dan vektor y menggunakan metode substitusi mundur
    x[n - 1][0] = y[n - 1][0] / A[n - 1][n - 1]
    for j in range(n - 2, -1, -1):
        S = 0
        for i in range(j + 1, n):
            S = S + A[j][i] * x[i][0]
        x[j][0] = (y[j][0] - S) / A[j][j]

    print('Solusi SPL (y):')
    for i in range(n):
        print(f'y{i + 1} = {y[i][0]}')  # Mencetak solusi y

    print('Solusi SPL (x):')
    for i in range(n):
        print(f'x{i + 1} = {x[i][0]}')  # Mencetak solusi x


# Meminta input matriks A dari pengguna
n = int(input("Masukkan ukuran matriks (n x n): "))  # Meminta ukuran matriks dari pengguna
A = np.zeros((n, n))  # Membuat matriks n x n dengan elemen nol
print(f"Masukkan elemen-elemen matriks A ({n}x{n}):")  # Meminta elemen-elemen matriks A dari pengguna
for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"A[{i + 1}][{j + 1}]: "))  # Meminta elemen matriks A

# Meminta input matriks b dari pengguna
b = np.zeros((n, 1))  # Membuat vektor nol b
print("Masukkan elemen-elemen matriks B:")  # Meminta elemen-elemen vektor b dari pengguna
for i in range(n):
    b[i][0] = float(input(f"B[{i + 1}]: "))  # Meminta elemen vektor b

# Memanggil fungsi LU dengan matriks A dan b yang dimasukkan oleh pengguna
LU(A, b)
