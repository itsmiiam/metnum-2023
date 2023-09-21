'''
Oktavina Zahra Rahmawati (2207287)
METODE BAGI DUA
No. 2
1. Buatlah modifikasi fungsi ketika kriteria program berhenti adalah sudah mencapai pada iterasi ke-n
2. Buatlah modifikasi agar user dapat menginputkan fungsi maupun batas akar dan galatnya
3. Buatlah modifikasi agar akarnya dapat ditampilkan dalam bentuk grafik
'''

import numpy as np
import matplotlib.pyplot as plt

# Fungsi my_bisection digunakan untuk mengimplementasikan metode Bagi Dua
def my_bisection(func, a, b, tol=1e-6, max_iterations=100):
    iterations = 0
    results = []  # Menyimpan hasil iterasi untuk grafik

    while iterations < max_iterations: # Melakukan iterasi hingga mencapai batas maksimal iterasi
        c = (a + b) / 2
        results.append(c)  # Menyimpan nilai c pada setiap iterasi
        if func(c) == 0 or (b - a) / 2 < tol: # Kondisi berhenti jika akar sudah ditemukan atau toleransi telah terpenuhi
            return c, results
        if np.sign(func(c)) == np.sign(func(a)): # Memperbarui batas a atau b berdasarkan tanda fungsi di titik c
            a = c
        else:
            b = c
        iterations += 1

    return None, results # Jika tidak ada akar yang ditemukan dalam jumlah maksimal iterasi, mengembalikan None

# Fungsi plot_bisection_results digunakan untuk mengeksekusi metode Bagi Dua dan menampilkan hasilnya
def plot_bisection_results(func, a, b, tol=1e-6, max_iterations=100):
    root, results = my_bisection(func, a, b, tol, max_iterations)

    if root is not None:
        print("Akar yang ditemukan:", root)
    else:
        print("Metode Bagi Dua tidak konvergen.")

    # Membuat array x dengan titik-titik untuk plotting fungsi
    x = np.linspace(a, b, 100)
    y = np.vectorize(func)(x)

    # Menampilkan grafik fungsi, titik-titik iterasi, dan garis horizontal
    plt.plot(x, y, label='f(x)')
    plt.scatter(results, np.vectorize(func)(results), c='red', marker='x', label='Iterasi')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Metode Bagi Dua')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Meminta input dari pengguna untuk fungsi, batas, dan parameter lainnya
    func_str = input("Masukkan fungsi (gunakan 'x' sebagai variabel): ")
    func = lambda x: eval(func_str)
    a = float(input("Masukkan batas bawah: "))
    b = float(input("Masukkan batas atas: "))
    max_iterations = int(input("Masukkan jumlah maksimal iterasi: "))
    tol = float(input("Masukkan toleransi galat: "))

    plot_bisection_results(func, a, b, tol, max_iterations)  # Menampilkan hasil metode Bagi Dua
 
