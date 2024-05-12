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

        cursor.execute("SELECT nada_ori, intonasi_ori, volume_ori FROM audio_data")

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

# Hasil Perhitugnan
@app.route('/HasilSingleAudio')
def hasil_single_audio_page():
    data = get_data_from_database()  # Assuming this function retrieves data from the database
    nada = session.get('nada')
    intonasi = session.get('intonasi')
    volume = session.get('volume')
    file_name = session.get('file_name')

    if nada is not None and intonasi is not None and volume is not None:
        # Inisialisasi matriks koefisien
        A_augmented = np.array([[nada, intonasi, volume]])

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
        if len(A_augmented) > 0:
            w1 = A_augmented[0, 0]
            w2 = A_augmented[0, 1]
            w3 = A_augmented[0, 2]
            b = 0  # Tidak ada elemen b dalam matriks A_augmented

            return render_template('hasil_singleaudio.html', nada=nada, intonasi=intonasi, volume=volume, file_name=file_name, w1=w1, w2=w2, w3=w3, b=b, data=data)
        else:
            return "Error occurred in solving linear equations."

    else:
        return "Error occurred. Please try again later."
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
