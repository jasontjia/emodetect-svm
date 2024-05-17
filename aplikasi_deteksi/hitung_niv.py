import librosa
import numpy as np

# Muat file audio
y, sr = librosa.load('D:/De La Salle/SEM 8/Tugas Akhir/aplikasi_deteksi/aplikasi_deteksi/audio_ori/test4.wav')

# Hitung nilai nada dari audio
pitch, _ = librosa.core.piptrack(y=y, sr=sr)

# Hitung nilai intonasi
pitch_values = pitch[pitch > 0]
median_pitch = np.median(pitch_values)
pitch_diff = np.diff(pitch_values)
intonasi = np.mean(np.abs(pitch_diff)) if len(pitch_diff) > 0 else 0

# Hitung nilai volume
rms = np.sqrt(np.mean(y**2))

# Cetak nilai nada, intonasi, dan volume
print(' (X1) Nada:', median_pitch)
print(' (X2) Intonasi:', intonasi)
print(' (X3) Volume:', rms)