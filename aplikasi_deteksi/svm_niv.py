import librosa
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Muat file audio
y, sr = librosa.load('D:/De La Salle/SEM 8/Tugas Akhir/aplikasi_deteksi/aplikasi_deteksi/audio_ori/test5.wav')

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
print(' (X1) Pitch:', median_pitch)
print(' (X2) Intonasi:', intonasi)
print(' (X3) Volume:', rms)