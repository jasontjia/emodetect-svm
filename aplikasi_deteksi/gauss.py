import numpy as np

# Sistem persamaan linear
# Persamaan 1: w1*15 + w2*25 + w3*35 + b >= 1
# Persamaan 2: w1*30 + w2*20 + w3*10 + b >= 1
# Persamaan 3: w1*25 + w2*35 + w3*15 + b >= 1

# Matriks koefisien
A = np.array([[15.0, 25.0, 35.0],
              [30.0, 20.0, 10.0],
              [25.0, 35.0, 15.0]])

# Vektor hasil
b_vector = np.array([1.0, 1.0, 1.0])

# Matriks augmented
A_augmented = np.hstack((A, b_vector.reshape(-1, 1)))

# Langkah eliminasi Gauss
for i in range(len(A_augmented)):
    # Pilih baris pivoting
    pivot_row = A_augmented[i]
    
    # Cek apakah elemen diagonal nol
    if pivot_row[i] == 0:
        continue
    
    # Normalisasi baris pivoting
    pivot_row = pivot_row / pivot_row[i]
    A_augmented[i] = pivot_row
    
    # Eliminasi
    for j in range(i + 1, len(A_augmented)):
        factor = A_augmented[j, i]
        A_augmented[j] -= factor * pivot_row

# Solusi
w1 = A_augmented[0, -2]
w2 = A_augmented[1, -2]
w3 = A_augmented[2, -3]
b = A_augmented[0, -1]

print("Nilai w1:", w1)
print("Nilai w2:", w2)
print("Nilai w3:", w3)
print("Nilai b:", b)

# Persamaan hyperplane
print("Persamaan hyperplane:")
print(f"{w1}x1 + {w2}x2 + {w3}x3 + {b}")

# Input nilai x1, x2, x3
x1 = float(input("Masukkan nilai x1: "))
x2 = float(input("Masukkan nilai x2: "))
x3 = float(input("Masukkan nilai x3: "))

# Hitung hasil akhir
hasil = w1*x1 + w2*x2 + w3*x3 + (b)
print("Hasil akhir:", hasil)
