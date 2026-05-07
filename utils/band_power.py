import numpy as np
from scipy.signal import welch

def calculate_band_power(signal, fs=256):

    freqs, psd = welch(signal, fs=fs, nperseg=256)

    # Define bands
    alpha_band = (8, 13)
    beta_band = (13, 30)
    gamma_band = (30, 45)

    def band_power(band):
        low, high = band
        idx = np.logical_and(freqs >= low, freqs <= high)
        return np.sum(psd[idx])

    alpha_power = band_power(alpha_band)
    beta_power = band_power(beta_band)
    gamma_power = band_power(gamma_band)

    total = alpha_power + beta_power + gamma_power

    alpha_pct = (alpha_power / total) * 100
    beta_pct = (beta_power / total) * 100
    gamma_pct = (gamma_power / total) * 100

    return alpha_pct, beta_pct, gamma_pct