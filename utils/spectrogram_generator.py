import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import os
import cv2

def generate_spectrogram(signal_data, fs=256):

    if not os.path.exists("assets"):
        os.makedirs("assets")

    frequencies, times, Sxx = signal.spectrogram(
        signal_data,
        fs=fs,
        nperseg=128,
        noverlap=64
    )

    Sxx_dB = 10 * np.log10(Sxx + 1e-10)

    plt.figure(figsize=(10, 5))

    plt.pcolormesh(
        times,
        frequencies,
        Sxx_dB,
        shading='gouraud',
        cmap='jet'
    )

    # EEG Frequency Focus
    plt.ylim(0, 50)

    # Highlight EEG Bands
    plt.axhspan(8, 13, alpha=0.2, color='green', label="Alpha (8-13 Hz)")
    plt.axhspan(13, 30, alpha=0.2, color='yellow', label="Beta (13-30 Hz)")
    plt.axhspan(30, 45, alpha=0.2, color='red', label="Gamma (30-45 Hz)")

    plt.ylabel("Frequency (Hz)", fontsize=12)
    plt.xlabel("Time (Seconds)", fontsize=12)
    plt.title("EEG Spectrogram with Band Highlighting", fontsize=14)

    plt.colorbar(label="Power (dB)")
    plt.legend(loc="upper right")

    plt.tight_layout()

    save_path = "assets/spectrogram_full.png"
    plt.savefig(save_path, dpi=300)
    plt.close()

    # ------------------------------
    # CNN READY VERSION (224x224)
    # ------------------------------
    image = cv2.imread(save_path)
    image = cv2.resize(image, (224, 224))
    cnn_path = "assets/spectrogram_cnn.png"
    cv2.imwrite(cnn_path, image)

    return save_path, cnn_path