import numpy as np

def generate_signal(alpha, beta, gamma, fs=256, duration=3):

    t = np.linspace(0, duration, fs * duration)

    alpha_wave = alpha * np.sin(2 * np.pi * 10 * t)
    beta_wave  = beta  * np.sin(2 * np.pi * 20 * t)
    gamma_wave = gamma * np.sin(2 * np.pi * 40 * t)

    noise = np.random.normal(0, 1.5, len(t))

    eeg_signal = alpha_wave + beta_wave + gamma_wave + noise

    return eeg_signal