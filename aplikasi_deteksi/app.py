from flask import Flask, render_template, redirect, request, send_from_directory, session
import mysql.connector
import librosa
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Secret key for session management

# Konfigurasi koneksi ke database
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_database = 'audio'

# Path ke folder audio_ori di luar direktori static
AUDIO_FOLDER = os.path.join(app.root_path, 'audio_ori')

# Fungsi untuk mendapatkan data dari database
def get_data_from_database():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT nada_ori, intonasi_ori, volume_ori, label_manual FROM audio_data")

        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return data

    except Exception as e:
        print("Error:", e)
        return None

# Fungsi untuk mengekstrak fitur audio
def extract_audio_features(audio_file):
    try:
        # Muat file audio
        y, sr = librosa.load(audio_file)

        # Hitung nilai nada dari audio
        pitch, _ = librosa.core.piptrack(y=y, sr=sr)
        
        # Hitung nilai intonasi
        pitch_values = pitch[pitch > 0]
        median_pitch = np.median(pitch_values)
        pitch_diff = np.diff(pitch_values)
        intonation = np.mean(np.abs(pitch_diff)) if len(pitch_diff) > 0 else 0

        # Hitung nilai volume
        rms = np.sqrt(np.mean(y**2))

        # Konversi tipe data numpy.float32 ke float
        median_pitch = float(median_pitch)
        intonation = float(intonation)
        rms = float(rms)

        return median_pitch, intonation, rms

    except Exception as e:
        print("Error extracting audio features:", e)
        return None, None, None

# Route untuk mengirimkan file audio
@app.route('/audio/<path:filename>')
def download_file(filename):
    return send_from_directory(AUDIO_FOLDER, filename)

# Route untuk setiap halaman web
@app.route('/')  
def index():
    return redirect('/Beranda')

@app.route('/Beranda')
def beranda():
    return render_template('index.html')

@app.route('/SingleAudio')
def single_audio():
    return render_template('single_audio.html')

@app.route('/DataLatih')
def data_latih():
    return render_template('data_latih.html')

@app.route('/HasilDataLatih')
def hasil_data_latih():
    return render_template('hasil_datalatih.html')

@app.route('/HasilSingleAudio', methods=['POST'])
def hasil_single_audio():  
    if 'file' not in request.files:
        return redirect('/SingleAudio')

    audio_file = request.files['file']

    if audio_file.filename == '':
        return redirect('/SingleAudio')

    # Dapatkan nama file audio
    file_name = audio_file.filename

    # Simpan file sementara
    temp_file_path = 'temp_audio.wav'
    audio_file.save(temp_file_path)

    # Ekstrak fitur audio
    nada, intonasi, volume = extract_audio_features(temp_file_path)

    # Hapus file sementara
    os.remove(temp_file_path)

    if nada is not None and intonasi is not None and volume is not None:
        try:
            connection = mysql.connector.connect(
                host=db_host,
                user=db_user,
                password=db_password,
                database=db_database
            )

            cursor = connection.cursor()

            # Masukkan data ke database
            cursor.execute("INSERT INTO audio_data (nama_audio, nada_ori, intonasi_ori, volume_ori) VALUES (%s, %s, %s, %s)", (file_name, nada, intonasi, volume))
            connection.commit()

            # Simpan nilai-nilai dalam session
            session['nada'] = nada
            session['intonasi'] = intonasi
            session['volume'] = volume
            session['file_name'] = file_name

            cursor.close()
            connection.close()

            return redirect('/HasilSingleAudio')

        except Exception as e:
            print("Error inserting data into database:", e)
            print("Type of feature values:", type(nada), type(intonasi), type(volume))
            return "Error occurred. Please try again later."

    else:
        return "Error extracting audio features. Please try again with a different file."

# Perhitungan Algoritma SVM RBF
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
        calculation_step = f"Perhitungan prediksi untuk sampel uji {i+1}:\n"
        # Hitung nilai prediksi untuk sampel uji saat ini
        for j in range(n_train):
            # Hitung nilai kernel antara sampel latih dan sampel uji
            kernel_value = rbf_kernel(X_train[j], X_test[i], gamma)
            # Simpan nilai kernel ke dalam list
            kernel_values.append((X_train[j], X_test[i], kernel_value))
            # Hitung nilai prediksi dengan menambahkan kontribusi dari setiap sampel latih
            prediction += y_train[j] * kernel_value
            calculation_step += f"  Kontribusi dari sampel latih {j+1}: y_train={y_train[j]}, kernel={kernel_value}, kontribusi={y_train[j] * kernel_value}\n"
        # Simpan nilai prediksi sebelum mengambil tanda
        prediction_values[i] = prediction
        # Simpan langkah perhitungan
        calculation_step += f"  Nilai prediksi sebelum tanda: {prediction}\n"
        calculation_steps.append(calculation_step)
        # Tentukan kelas prediksi berdasarkan tanda dari prediksi akhir
        predictions[i] = np.sign(prediction)
    
    return predictions.astype(int), prediction_values, kernel_values, calculation_steps

@app.route('/HasilSingleAudio')
def hasil_single_audio_page():
    data = get_data_from_database()
    if data is None:
        return "Terjadi kesalahan saat mengambil data dari database."

    nada = session.get('nada')
    intonasi = session.get('intonasi')
    volume = session.get('volume')
    file_name = session.get('file_name')

    if nada is not None and intonasi is not None and volume is not None:
        nada = float(nada)
        intonasi = float(intonasi)
        volume = float(volume)

        angry_samples = np.array([
            [entry['nada_ori'], entry['intonasi_ori'], entry['volume_ori']]
            for entry in data if entry['label_manual'] == 'Marah'
        ], dtype=float)

        non_angry_samples = np.array([
            [entry['nada_ori'], entry['intonasi_ori'], entry['volume_ori']]
            for entry in data if entry['label_manual'] == 'Tidak Marah'
        ], dtype=float)
        
        X_train = np.vstack((angry_samples, non_angry_samples))
        y_train = np.array([-1] * len(angry_samples) + [1] * len(non_angry_samples))

        new_sample = np.array([nada, intonasi, volume], dtype=float)
        gamma = 0.01

        # Lakukan prediksi menggunakan SVM dengan kernel RBF
        predicted_class, prediction_value, kernel_values, calculation_steps = predict_svm_rbf(X_train, y_train, [new_sample], gamma)

        if predicted_class == -1:
            prediction_result = "Marah"
        else:
            prediction_result = "Tidak Marah"

        kernel_values_display = []  # List untuk menyimpan nilai kernel RBF

        # Loop untuk menambahkan nilai kernel RBF ke dalam list kernel_values_display
        for (x_train, x_test, kernel_value) in kernel_values:
            kernel_values_display.append(f"Kernel antara {x_train} dan {x_test}: {kernel_value}")

        # Simpan nilai prediksi 
        prediction_value_display = prediction_value[0]
        
        return render_template('hasil_singleaudio.html', nada=nada, intonasi=intonasi, volume=volume, file_name=file_name, data=data, prediction_result=prediction_result, kernel_values_display=kernel_values_display, prediction_value_display=prediction_value_display, calculation_steps=calculation_steps)
    
    return "Data tidak lengkap untuk melakukan prediksi."

# Form Unggah
@app.route('/FormUnggah', methods=['GET', 'POST'])
def form_unggah():  
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect('/FormUnggah')

        audio_file = request.files['file']

        if audio_file.filename == '':
            return redirect('/FormUnggah')

        # Dapatkan nama file audio
        file_name = audio_file.filename

        # Simpan file sementara
        temp_file_path = 'temp_audio.wav'
        audio_file.save(temp_file_path)

        # Ekstrak fitur audio
        nada, intonasi, volume = extract_audio_features(temp_file_path)

        # Hapus file sementara
        os.remove(temp_file_path)

        if nada is not None and intonasi is not None and volume is not None:
            try:
                connection = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_database
                )

                cursor = connection.cursor()

                # Masukkan data ke database
                cursor.execute("INSERT INTO audio_data (nama_audio, nada_ori, intonasi_ori, volume_ori) VALUES (%s, %s, %s, %s)", (file_name, nada, intonasi, volume))
                connection.commit()

                # Simpan nilai-nilai dalam session
                session['nada'] = nada
                session['intonasi'] = intonasi
                session['volume'] = volume
                session['file_name'] = file_name

                cursor.close()
                connection.close()

                return render_template('form-unggah.html', nada=nada, intonasi=intonasi, volume=volume, file_name=file_name)

            except Exception as e:
                print("Error inserting data into database:", e)
                print("Type of feature values:", type(nada), type(intonasi), type(volume))
                return "Error occurred. Please try again later."

        else:
            return "Error extracting audio features. Please try again with a different file."

    elif request.method == 'GET':
        # Nilai default jika belum ada file audio yang diproses
        nada = None
        intonasi = None
        volume = None
        return render_template('form-unggah.html')

if __name__ == '__main__':
    app.run(debug=True)