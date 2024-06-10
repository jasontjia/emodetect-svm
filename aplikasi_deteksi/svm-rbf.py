import numpy as np

# Fungsi kernel RBF
def rbf_kernel(x, x_prime, gamma):
    distance_squared = np.sum((x - x_prime)**2)
    kernel_value = np.exp(-gamma * distance_squared)
    return kernel_value

# Prediksi kelas menggunakan SVM dengan kernel RBF
def predict_svm_rbf(X_train, y_train, X_test, gamma):
    n_train = len(X_train)
    n_test = len(X_test)
    predictions = np.zeros(n_test)
    prediction_values = np.zeros(n_test)  # Array untuk menyimpan nilai prediksi sebelum mengambil tanda
    kernel_values = []  # List untuk menyimpan nilai kernel RBF
    calculation_steps = []  # List untuk menyimpan langkah-langkah perhitungan
    
    # Looping untuk setiap sampel di data uji
    for i in range(n_test):
        prediction = 0
        calculation_step = f"Perhitungan untuk sample uji {i+1}:\n"
        # List untuk menyimpan nilai kernel untuk sample uji ini
        kernel_values_per_test = []
        # Hitung nilai prediksi untuk sampel uji saat ini
        for j in range(n_train):
            # Hitung nilai kernel antara sampel latih dan sampel uji
            kernel_value = rbf_kernel(X_train[j], X_test[i], gamma)
            # Simpan nilai kernel ke dalam list
            kernel_values_per_test.append((X_train[j], X_test[i], kernel_value))
            # Hitung nilai prediksi dengan menambahkan kontribusi dari setiap sampel latih
            contrib = y_train[j] * kernel_value
            if contrib == 0.0:
                contrib = 0.0  # Pastikan nilai kontribusi adalah 0.0 dan tidak dianggap negatif
            prediction += contrib
            calculation_step += f"  Kontribusi dari data uji {j+1}: y_train={y_train[j]}, kernel={kernel_value:.3f}, kontribusi={contrib:.3f}\n"
        # Simpan nilai kernel per sample uji ke dalam list utama
        kernel_values.append(kernel_values_per_test)
        # Simpan nilai prediksi sebelum mengambil tanda
        prediction_values[i] = prediction
        # Simpan langkah perhitungan
        calculation_step += f"  Nilai Klasifikasi : {prediction:.3f}\n"
        calculation_steps.append(calculation_step)
        # Tentukan kelas prediksi berdasarkan tanda dari prediksi akhir
        predictions[i] = np.sign(prediction)
    
    return predictions.astype(int), prediction_values, kernel_values, calculation_steps

# Contoh data fitur untuk dua kelas: marah dan tidak marah
angry_samples = np.array([[1773.406, 3.432, 0.003],
                          [1365.412, 3.637, 0.007]])  # Fixed to have 3 features

non_angry_samples = np.array([[1727.075, 3.396, 0.003], 
                              [1139.116, 4.283, 0.008],
                              [1776.637, 3.533, 0.004],
                              [2209.671, 5.591, 0.070]])

# Gabungkan kedua set data untuk pelatihan
X_train = np.vstack((angry_samples, non_angry_samples))

# Label untuk kedua kelas
y_train = np.array([-1] * len(angry_samples) + [1] * len(non_angry_samples))

# Prediksi kelas untuk contoh baru
# Misalnya, kita memiliki contoh baru sebagai berikut:
new_sample = np.array([[1774.55, 3.387, 0.028]])

# Parameter gamma untuk kernel RBF
gamma = 0.01

# Lakukan prediksi menggunakan SVM dengan kernel RBF
predicted_class, prediction_value, kernel_values, calculation_steps = predict_svm_rbf(X_train, y_train, new_sample, gamma)

# Print hasil prediksi
for i, pred in enumerate(predicted_class):
    if pred == -1:
        print(f"Sample {i+1} Prediksi: Marah")
    else:
        print(f"Sample {i+1} Prediksi: Tidak Marah")

# Print nilai kernel RBF per sample uji
print("\nNilai kernel RBF per sample uji:")
for test_index, test_kernels in enumerate(kernel_values):
    print(f"\nSample uji {test_index+1}:")
    for (x_train, x_test, kernel_value) in test_kernels:
        print(f"  Kernel antara {', '.join(map('{:.3f}'.format, x_test.tolist()))} dan {', '.join(map('{:.3f}'.format, x_train.tolist()))}: {kernel_value:.3f}")

# Print langkah-langkah perhitungan
print("\nLangkah-langkah perhitungan:")
for step in calculation_steps:
    print(step)