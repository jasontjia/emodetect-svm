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
    
    # Looping untuk setiap sampel di data uji
    for i in range(n_test):
        prediction = 0
        # Hitung nilai prediksi untuk sampel uji saat ini
        for j in range(n_train):
            # Hitung nilai kernel antara sampel latih dan sampel uji
            kernel_value = rbf_kernel(X_train[j], X_test[i], gamma)
            # Hitung nilai prediksi dengan menambahkan kontribusi dari setiap sampel latih
            prediction += y_train[j] * kernel_value
        # Tentukan kelas prediksi berdasarkan tanda dari prediksi akhir
        predictions[i] = np.sign(prediction)
    return predictions.astype(int)

# Contoh data fitur untuk dua kelas: marah dan tidak marah
angry_samples = np.array([[100, 0.5, 0.8],
                           [110, 0.6, 0.7],
                           [90, 0.4, 0.9]])

non_angry_samples = np.array([[120, 0.7, 0.6],
                               [115, 0.8, 0.5],
                               [125, 0.9, 0.4]])

# Gabungkan kedua set data untuk pelatihan
X_train = np.vstack((angry_samples, non_angry_samples))

# Label untuk kedua kelas
y_train = np.array([-1] * len(angry_samples) + [1] * len(non_angry_samples))

# Prediksi kelas untuk contoh baru
# Misalnya, kita memiliki contoh baru sebagai berikut:
new_sample = np.array([105, 0.55, 0.75])

# Parameter gamma untuk kernel RBF
gamma = 0.01

# Lakukan prediksi menggunakan SVM dengan kernel RBF
predicted_class = predict_svm_rbf(X_train, y_train, [new_sample], gamma)[0]

# Print hasil prediksi
if predicted_class == -1:
    print("Prediksi: Marah")
else:
    print("Prediksi: Tidak Marah")
