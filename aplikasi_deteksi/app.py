from flask import Flask, render_template, redirect, request, jsonify, send_from_directory, session
from werkzeug.utils import secure_filename
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

# Fungsi untuk mendapatkan data uji dari database
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

# Fungsi untuk mendapatkan data uji dari database
def tarik_database():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT nada_ori_latih, intonasi_ori_latih, volume_ori_latih, label_manual_latih FROM audio_latih")

        data_latih = cursor.fetchall()

        cursor.close()
        connection.close()

        return data_latih

    except Exception as e:
        print("Error:", e)
        return None
    
# Fungsi untuk menyimpan data training ke database
def simpan_data_ke_database(data):
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )
        cursor = connection.cursor()

        # Lakukan loop untuk setiap baris data dan masukkan ke dalam database
        for row in data:
            query = """
            INSERT INTO audio_latih (nama_audio_latih, nada_ori_latih, intonasi_ori_latih, volume_ori_latih, label_manual_latih) 
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (row['nama_audio_latih'], row['nada_ori_latih'], row['intonasi_ori_latih'], row['volume_ori_latih'], row['label_manual_latih']))

        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print("Database Error:", e)
        raise

# Fungsi untuk mengekstrak fitur audio
def extract_audio_features(audio_file):
    try:
        # Muat file audio
        y, sr = librosa.load(audio_file)

        # Hitung nilai nada dari audio
        pitch, _ = librosa.core.piptrack(y=y, sr=sr)
        pitch_values = pitch[pitch > 0]
        
        # Hitung nilai intonasi
        median_pitch = np.median(pitch_values)
        pitch_diff = np.diff(pitch_values)
        intonation = np.mean(np.abs(pitch_diff)) if len(pitch_diff) > 0 else 0

        # Hitung nilai volume
        rms = np.sqrt(np.mean(y**2))

        # Konversi tipe data numpy.float32 ke float
        median_pitch = round(float(median_pitch), 3)
        intonation = round(float(intonation), 3)
        rms = round(float(rms), 3)

        return median_pitch, intonation, rms

    except Exception as e:
        print("Error extracting audio features:", e)
        return None, None, None

# Define the directory where audio files are stored
AUDIO_ORI_UJI_FOLDER = 'data uji/audio_ori_uji'
MARAH_UJI_FOLDER = 'data uji/marah_uji'
TIDAKMARAH_UJI_FOLDER = 'data uji/tidakmarah_uji'

# Route untuk mengirimkan file audio
@app.route('/audio/<folder>/<path:filename>')
def download_file(folder, filename):
    if folder == 'audio_ori_uji':
        directory = AUDIO_ORI_UJI_FOLDER
    elif folder == 'marah_uji':
        directory = MARAH_UJI_FOLDER
    elif folder == 'tidakmarah_uji':
        directory = TIDAKMARAH_UJI_FOLDER
    else:
        return "Invalid folder", 404
    return send_from_directory(directory, filename)

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
    
##Form Data Latih
@app.route('/DataLatih', methods=['GET', 'POST'])
def data_latih():
    if request.method == 'POST':
        audio_files = request.files.getlist('audioFiles')
        data = []
        for audio_file in audio_files:
            if audio_file:
                file_name = secure_filename(audio_file.filename)
                nada, intonasi, volume = extract_audio_features(audio_file)
                if nada is not None:
                    data.append((file_name, nada, intonasi, volume))
        return render_template('data_latih.html', data=data, enumerate=enumerate)
    return render_template('data_latih.html')

## Ekstraksi Audio Data Latih
def extract_audio_features(audio_file):
    try:
        y, sr = librosa.load(audio_file)
        pitch, _ = librosa.core.piptrack(y=y, sr=sr)
        pitch_values = pitch[pitch > 0]
        median_pitch = round(float(np.median(pitch_values)), 3)
        pitch_diff = np.diff(pitch_values)
        intonation = round(float(np.mean(np.abs(pitch_diff))), 3) if len(pitch_diff) > 0 else 0.000
        rms = round(float(np.sqrt(np.mean(y**2))), 3)
        
        return median_pitch, intonation, rms
    except Exception as e:
        print("Error extracting audio features:", e)
        return None, None, None

# Hasil Data Latih
@app.route('/HasilDataLatih', methods=['POST'])
def hasil_data_latih():
    if request.method == 'POST':
        try:
            audio_latih = request.get_json()  # Mendapatkan data JSON dari permintaan POST
            print("Received Data:", audio_latih)
            if audio_latih:
                simpan_data_ke_database(audio_latih)  # Memanggil fungsi untuk menyimpan data ke database
                return jsonify({"message": "Data berhasil disimpan ke dalam database."}), 200
            else:
                return jsonify({"error": "Tidak ada data yang diterima."}), 400
        except Exception as e:
            print("Error:", e)
            return jsonify({"error": "Terjadi kesalahan saat menyimpan data ke database."}), 500
    else:
        return jsonify({"error": "Metode yang digunakan tidak valid."}), 405

# Perhitungan SVM RBF Data Latih
def predict_svm_rbf_data_latih(X_train, y_train, X_test, gamma):
    n_train = len(X_train)
    n_test = len(X_test)
    predictions = np.zeros(n_test)
    prediction_values = np.zeros(n_test)  # Array untuk menyimpan nilai prediksi sebelum mengambil tanda
    kernel_values = []  # List untuk menyimpan nilai kernel RBF
    calculation_steps = []  # List untuk menyimpan langkah-langkah perhitungan
    
    # Looping untuk setiap sampel di data uji
    for i in range(n_test):
        prediction = 0
        calculation_step = f"Perhitungan untuk data baru { i+1} :\n "
        # Hitung nilai prediksi untuk sampel uji saat ini
        for j in range(n_train):
            # Hitung nilai kernel antara sampel latih dan sampel uji
            kernel_value = rbf_kernel(X_train[j], X_test[i], gamma)
            # Simpan nilai kernel ke dalam list
            kernel_values.append((X_train[j], X_test[i], kernel_value))
            # Hitung nilai prediksi dengan menambahkan kontribusi dari setiap sampel latih
            contrib = y_train[j] * kernel_value
            if contrib == 0.0:
                contrib = 0.0  # Pastikan nilai kontribusi adalah 0.0 dan tidak dianggap negatif
            prediction += contrib
            calculation_step += f"  Kontribusi dari data latih {j+1}: y_train={y_train[j]}, kernel={kernel_value:.3f}, kontribusi={contrib:.3f}\n"
        # Simpan nilai prediksi sebelum mengambil tanda
        prediction_values[i] = prediction
        # Simpan langkah perhitungan
        calculation_step += f"  Nilai Klasifikasi : {prediction:.3f}\n"
        calculation_steps.append(calculation_step)
        # Tentukan kelas prediksi berdasarkan tanda dari prediksi akhir
        predictions[i] = np.sign(prediction)
    
    return predictions.astype(int), prediction_values, kernel_values, calculation_steps

## Hasil Data Latih
@app.route('/HasilDataLatih')
def hasil_data_latih_():
    data_latih = tarik_database()
    if data_latih is None:
        return "Terjadi kesalahan saat mengambil data dari database."

    # Pisahkan data dari database ke dalam angry_samples dan non_angry_samples
    angry_samples = np.array([
        [round(float(entry['nada_ori_latih']), 3), round(float(entry['intonasi_ori_latih']), 3), round(float(entry['volume_ori_latih']), 3)]
        for entry in data_latih if entry['label_manual_latih'] == 'Marah'
    ], dtype=float)

    non_angry_samples = np.array([
        [round(float(entry['nada_ori_latih']), 3), round(float(entry['intonasi_ori_latih']), 3), round(float(entry['volume_ori_latih']), 3)]
        for entry in data_latih if entry['label_manual_latih'] == 'Tidak Marah'
    ], dtype=float)
    
    # Gabungkan kedua set data untuk pelatihan
    X_train = np.vstack((angry_samples, non_angry_samples))
    y_train = np.array([-1] * len(angry_samples) + [1] * len(non_angry_samples))
    
    gamma = 0.01

    # Ambil sampel terbaru dari database
    latest_entry = data_latih[-1]
    new_sample = np.array([[round(float(latest_entry['nada_ori_latih']), 3), round(float(latest_entry['intonasi_ori_latih']), 3), round(float(latest_entry['volume_ori_latih']), 3)]], dtype=float)

    # Prediksi untuk sampel baru
    new_predicted_class, new_prediction_values, new_kernel_values, new_calculation_steps = predict_svm_rbf_data_latih(X_train, y_train, new_sample, gamma)
    new_prediction_result = "Marah" if new_predicted_class[0] == -1 else "Tidak Marah"

    new_kernel_values_display = []

    for (x_train, x_test, kernel_value) in new_kernel_values:
        formatted_x_train = ', '.join([f"{value:.3f}" for value in x_train])
        formatted_x_test = ', '.join([f"{value:.3f}" for value in x_test])
        new_kernel_values_display.append(f"Kernel antara [{formatted_x_train}] dan [{formatted_x_test}]: {kernel_value:.3f}")

    # Gabungkan data dengan hasil prediksi untuk ditampilkan
    new_sample_result = {
        'nada': round(float(latest_entry['nada_ori_latih']), 3),
        'intonasi': round(float(latest_entry['intonasi_ori_latih']), 3),
        'volume': round(float(latest_entry['volume_ori_latih']), 3),
        'prediction_result': new_prediction_result,
        'prediction_value': round(new_prediction_values[0], 3)
    }

    return render_template('hasil_datalatih.html', new_sample_result=new_sample_result, new_kernel_values_display=new_kernel_values_display, new_calculation_steps=new_calculation_steps)

## Hasil Single Audio
@app.route('/HasilSingleAudio', methods=['POST'])
def hasil_single_audio():
    if 'file' not in request.files or 'label_manual' not in request.form:
        return redirect('/SingleAudio')

    audio_file = request.files['file']
    label_manual = request.form['label_manual']

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

    if nada is not None and intonasi is not None and volume is not None and label_manual:
        try:
            connection = mysql.connector.connect(
                host=db_host,
                user=db_user,
                password=db_password,
                database=db_database
            )

            cursor = connection.cursor()

            # Masukkan data ke database
            cursor.execute(
                "INSERT INTO audio_data (nama_audio, nada_ori, intonasi_ori, volume_ori, label_manual) VALUES (%s, %s, %s, %s, %s)",
                (file_name, nada, intonasi, volume, label_manual)
            )
            connection.commit()

            # Simpan nilai-nilai dalam session
            session['nada'] = nada
            session['intonasi'] = intonasi
            session['volume'] = volume
            session['file_name'] = file_name
            session['label_manual'] = label_manual

            cursor.close()
            connection.close()

            return redirect('/HasilSingleAudio')

        except Exception as e:
            print("Error inserting data into database:", e)
            return "Error occurred. Please try again later."

    else:
        return "Error extracting audio features. Please try again with a different file."

# Perhitungan SVM RBF Uji
def rbf_kernel(x, x_prime, gamma):
    distance_squared = np.sum((x - x_prime)**2)
    kernel_value = np.exp(-gamma * distance_squared)
    return kernel_value

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
        calculation_step = f"Perhitungan untuk data baru:\n"
        # Hitung nilai prediksi untuk sampel uji saat ini
        for j in range(n_train):
            # Hitung nilai kernel antara sampel latih dan sampel uji
            kernel_value = rbf_kernel(X_train[j], X_test[i], gamma)
            # Simpan nilai kernel ke dalam list
            kernel_values.append((X_train[j], X_test[i], kernel_value))
            # Hitung nilai prediksi dengan menambahkan kontribusi dari setiap sampel latih
            contrib = y_train[j] * kernel_value
            if contrib == 0.0:
                contrib = 0.0  # Pastikan nilai kontribusi adalah 0.0 dan tidak dianggap negatif
            prediction += contrib
            calculation_step += f"  Kontribusi dari data uji {j+1}: y_train={y_train[j]}, kernel={kernel_value:.3f}, kontribusi={contrib:.3f}\n"
        # Simpan nilai prediksi sebelum mengambil tanda
        prediction_values[i] = prediction
        # Simpan langkah perhitungan
        calculation_step += f"  Nilai Klasifikasi : {prediction:.3f}\n"
        calculation_steps.append(calculation_step)
        # Tentukan kelas prediksi berdasarkan tanda dari prediksi akhir
        predictions[i] = np.sign(prediction)
    
    return predictions.astype(int), prediction_values, kernel_values, calculation_steps

## Hasil Single Audio 
@app.route('/HasilSingleAudio')
def hasil_single_audio_page():
    data = get_data_from_database()
    if data is None:
        return "Terjadi kesalahan saat mengambil data dari database."

    nada = session.get('nada')
    intonasi = session.get('intonasi')
    volume = session.get('volume')
    file_name = session.get('file_name')
    label_manual = session.get('label_manual')

    if nada is not None and intonasi is not None and volume is not None:
        # Konversi nilai menjadi float dan membulatkannya menjadi 3 angka di belakang koma
        nada = round(float(nada), 3)
        intonasi = round(float(intonasi), 3)
        volume = round(float(volume), 3)

        # Pisahkan data dari database ke dalam angry_samples dan non_angry_samples
        angry_samples = np.array([
            [round(float(entry['nada_ori']), 3), round(float(entry['intonasi_ori']), 3), round(float(entry['volume_ori']), 3)]
            for entry in data if entry['label_manual'] == 'Marah'
        ], dtype=float)

        non_angry_samples = np.array([
            [round(float(entry['nada_ori']), 3), round(float(entry['intonasi_ori']), 3), round(float(entry['volume_ori']), 3)]
            for entry in data if entry['label_manual'] == 'Tidak Marah'
        ], dtype=float)
        
        # Exclude the labeled sample from the training data if it exists
        if label_manual == 'Marah':
            angry_samples = angry_samples[:-1] if len(angry_samples) > 0 else angry_samples
        elif label_manual == 'Tidak Marah':
            non_angry_samples = non_angry_samples[:-1] if len(non_angry_samples) > 0 else non_angry_samples
        
        # Gabungkan kedua set data untuk pelatihan
        X_train = np.vstack((angry_samples, non_angry_samples))
        y_train = np.array([-1] * len(angry_samples) + [1] * len(non_angry_samples))

        # Contoh baru (sampel baru)
        new_sample = np.array([[nada, intonasi, volume]], dtype=float)
        gamma = 0.01

        # Lakukan prediksi menggunakan SVM dengan kernel RBF
        predicted_class, prediction_value, kernel_values, calculation_steps = predict_svm_rbf(X_train, y_train, new_sample, gamma)

        if predicted_class[0] == -1:
            prediction_result = "Marah"
        else:
            prediction_result = "Tidak Marah"

        # Simpan hasil prediksi ke database
        try:
            connection = mysql.connector.connect(
                host=db_host,
                user=db_user,
                password=db_password,
                database=db_database
            )

            cursor = connection.cursor()

            cursor.execute(
                "UPDATE audio_data SET label_otomatis=%s WHERE nama_audio=%s",
                (prediction_result, file_name)
            )
            connection.commit()

            cursor.close()
            connection.close()

        except Exception as e:
            print("Error updating data in database:", e)
            return "Error occurred while updating the database. Please try again later."

        kernel_values_display = []  # List untuk menyimpan nilai kernel RBF

        # Loop untuk menambahkan nilai kernel RBF ke dalam list kernel_values_display
        for (x_train, x_test, kernel_value) in kernel_values:
            formatted_x_train = ', '.join([f"{value:.3f}" for value in x_train])
            formatted_x_test = ', '.join([f"{value:.3f}" for value in x_test])
            kernel_values_display.append(f"Kernel antara [{formatted_x_train}] dan [{formatted_x_test}]: {kernel_value:.3f}")

        # Simpan nilai prediksi 
        prediction_value_display = f"{prediction_value[0]:.3f}"
        
        return render_template('hasil_singleaudio.html', nada=nada, intonasi=intonasi, volume=volume, file_name=file_name, data=data, prediction_result=prediction_result, kernel_values_display=kernel_values_display, prediction_value_display=prediction_value_display, calculation_steps=calculation_steps)
    
    return "Data tidak lengkap untuk melakukan prediksi."


# Form Unggah Uji
@app.route('/FormUnggahUji', methods=['GET', 'POST'])
def form_unggah_uji():  
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect('/FormUnggahUji')

        audio_file = request.files['file']

        if audio_file.filename == '':
            return redirect('/FormUnggahUji')

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
                # Mendapatkan nilai label manual yang dipilih oleh pengguna
                label_manual = request.form['label']

                connection = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_database
                )

                cursor = connection.cursor()

                # Masukkan data ke database
                cursor.execute("INSERT INTO audio_data (nama_audio, nada_ori, intonasi_ori, volume_ori, label_manual) VALUES (%s, %s, %s, %s, %s)", (file_name, nada, intonasi, volume, label_manual))
                connection.commit()

                # Simpan nilai-nilai dalam session
                session['nada'] = nada
                session['intonasi'] = intonasi
                session['volume'] = volume
                session['file_name'] = file_name

                cursor.close()
                connection.close()

                return render_template('form-unggah-uji.html', nada=nada, intonasi=intonasi, volume=volume, file_name=file_name)

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
        return render_template('form-unggah-uji.html')
    
#Form Unggah Latih
@app.route('/FormUnggahLatih', methods=['GET', 'POST'])
def form_unggah_latih():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect('/FormUnggahLatih')

        audio_file = request.files['file']

        if audio_file.filename == '':
            return redirect('/FormUnggahLatih')

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
                # Mendapatkan nilai label manual yang dipilih oleh pengguna
                label_manual = request.form['label']

                connection = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_database
                )

                cursor = connection.cursor()

                # Masukkan data ke tabel audio_latih
                cursor.execute(
                    "INSERT INTO audio_latih (nama_audio_latih, nada_ori_latih, intonasi_ori_latih, volume_ori_latih, label_manual_latih) VALUES (%s, %s, %s, %s, %s)",
                    (file_name, nada, intonasi, volume, label_manual)
                )
                connection.commit()

                # Simpan nilai-nilai dalam session
                session['nada'] = nada
                session['intonasi'] = intonasi
                session['volume'] = volume
                session['file_name'] = file_name

                cursor.close()
                connection.close()

                return render_template('form-unggah-latih.html', nada=nada, intonasi=intonasi, volume=volume, file_name=file_name)

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
        return render_template('form-unggah-latih.html')


if __name__ == '__main__':
    app.run(debug=True)