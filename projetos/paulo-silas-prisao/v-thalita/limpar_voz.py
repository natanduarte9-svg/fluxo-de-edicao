"""Limpa a voz do edge-tts (MP3 24 kHz com chiado de compressão): redução de ruído espectral,
suaviza o "s" (de-esser) e corta o agudo onde só há chiado. Gera voz/f<k>_limpa.wav."""
import numpy as np, soundfile as sf, noisereduce as nr
from scipy.signal import butter, sosfilt, sosfiltfilt
for k in range(1, 7):
    x, sr = sf.read(f"voz/f{k}.wav"); x = x.astype(np.float32)
    y = nr.reduce_noise(y=x, sr=sr, stationary=True, prop_decrease=0.85, n_fft=1024)
    # de-esser: comprime só a faixa 5–9 kHz quando ela passa do limite
    band = sosfilt(butter(4, [5000, 9000], "band", fs=sr, output="sos"), y)
    env = np.sqrt(np.convolve(band ** 2, np.ones(240) / 240, mode="same")) + 1e-9
    thr = 0.035; g = np.minimum(1.0, (thr / env) ** 0.6)
    y = y - band * (1 - g)
    y = sosfiltfilt(butter(6, 9500, "low", fs=sr, output="sos"), y)   # tira o agudo do chiado
    y = sosfiltfilt(butter(2, 90, "high", fs=sr, output="sos"), y)
    sf.write(f"voz/f{k}_limpa.wav", y.astype(np.float32), sr)
    hp = lambda s: 20 * np.log10(np.sqrt((sosfilt(butter(4, 5000, "high", fs=sr, output="sos"), s) ** 2).mean()) + 1e-9)
    print(k, "agudo antes %.1f dB → depois %.1f dB" % (hp(x), hp(y)))
