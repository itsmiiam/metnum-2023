'''
OKTAVINA ZAHRA RAHMAWATI (2207287)
METODE BAGI DUA
No. 1
a. f(x) = x^3 - 2x + 1
'''

import numpy as np  # Mengimpor library NumPy untuk penggunaan fungsi np.sign()

def my_bisection(func, a, b, tol=1e-6, max_iterations=100):
    iterations = 0  # Menginisialisasi jumlah iterasi
    while iterations < max_iterations:  # Mulai loop iterasi
        c = (a + b) / 2  # Menghitung titik tengah interval
        if func(c) == 0 or (b - a) / 2 < tol:  # Cek kriteria berhenti
            return c  # Mengembalikan akar yang ditemukan
        if np.sign(func(c)) == np.sign(func(a)):  # Memeriksa tanda fungsi pada titik tengah dan a
            a = c  # Update batas bawah interval
        else:
            b = c  # Update batas atas interval
        iterations += 1  # Increment jumlah iterasi
    return None  # Mengembalikan None jika akar tidak ditemukan dalam maksimum iterasi

# Fungsi baru: f(x) = x^3 - 2x + 1
f = lambda x: x**3 - 2*x + 1  # Mendefinisikan fungsi f(x)

r1 = my_bisection(f, 0, 2, 0.1)  # Menggunakan metode bisection dengan toleransi 0.1
print("r1 =", r1)  # Mencetak akar yang ditemukan
print("f(r1) =", f(r1))  # Mencetak nilai f(r1)

r01 = my_bisection(f, 0, 2, 0.01)  # Menggunakan metode bisection dengan toleransi 0.01
print("r01 =", r01)  # Mencetak akar yang ditemukan
print("f(r01) =", f(r01))  # Mencetak nilai f(r01)
