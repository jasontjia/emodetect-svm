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
    
    # Looping untuk setiap sampel di data uji
    for i in range(n_test):
        prediction = 0
        # Hitung nilai prediksi untuk sampel uji saat ini
        for j in range(n_train):
            # Hitung nilai kernel antara sampel latih dan sampel uji
            kernel_value = rbf_kernel(X_train[j], X_test[i], gamma)
            # Simpan nilai kernel ke dalam list
            kernel_values.append((X_train[j], X_test[i], kernel_value))
            # Hitung nilai prediksi dengan menambahkan kontribusi dari setiap sampel latih
            prediction += y_train[j] * kernel_value
        # Simpan nilai prediksi sebelum mengambil tanda
        prediction_values[i] = prediction
        # Tentukan kelas prediksi berdasarkan tanda dari prediksi akhir
        predictions[i] = np.sign(prediction)
    
    return predictions.astype(int), prediction_values, kernel_values

# Contoh data fitur untuk dua kelas: marah dan tidak marah
angry_samples = np.array([[0, -1, 1],
                          [0, -1, 1],
                          [0, 1, 0]])

non_angry_samples = np.array( [[-1, -1, 0], 
                               [1, 0, 1],
                               [0, 1, -1]])

# Gabungkan kedua set data untuk pelatihan
X_train = np.vstack((angry_samples, non_angry_samples))

# Label untuk kedua kelas
y_train = np.array([-1] * len(angry_samples) + [1] * len(non_angry_samples))

# Prediksi kelas untuk contoh baru
# Misalnya, kita memiliki contoh baru sebagai berikut:
new_sample = np.array([1, 0, -1])

# Parameter gamma untuk kernel RBF
gamma = 0.01

# Lakukan prediksi menggunakan SVM dengan kernel RBF
predicted_class, prediction_value, kernel_values = predict_svm_rbf(X_train, y_train, [new_sample], gamma)

# Print hasil prediksi
if predicted_class[0] == -1:
    print("Prediksi: Marah")
else:
    print("Prediksi: Tidak Marah")

# Print nilai kernel RBF
print("\nNilai kernel RBF:")
for (x_train, x_test, kernel_value) in kernel_values:
    print(f"Kernel antara {x_train} dan {x_test}: {kernel_value}")

# Print nilai prediksi
print(f"Nilai Klasifikasi: {prediction_value[0]}")