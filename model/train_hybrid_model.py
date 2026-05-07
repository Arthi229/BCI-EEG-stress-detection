import numpy as np
import cv2
import os
from tensorflow.keras.utils import to_categorical
from utils.signal_generator import generate_signal
from utils.spectrogram_generator import generate_spectrogram
from utils.band_power import calculate_band_power


NUM_SAMPLES = 600
classes = ["Relaxed", "High Stress", "Normal"]

images = []
numeric_features = []
labels = []

print("Generating dataset...")

for i in range(NUM_SAMPLES):

    alpha = np.random.uniform(5, 40)
    beta = np.random.uniform(5, 40)
    gamma = np.random.uniform(5, 40)

    signal = generate_signal(alpha, beta, gamma)
    full_img, cnn_img = generate_spectrogram(signal)

    img = cv2.imread(cnn_img)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0

    alpha_pct, beta_pct, gamma_pct = calculate_band_power(signal)

    values = [alpha_pct, beta_pct, gamma_pct]
    max_idx = np.argmax(values)

    if max_idx == 0:
        label = 0  # Relaxed
    elif max_idx == 1:
        label = 1  # High Stress
    else:
        label = 2  # Normal

    images.append(img)
    numeric_features.append([alpha_pct, beta_pct, gamma_pct])
    labels.append(label)

images = np.array(images)
numeric_features = np.array(numeric_features)
labels = to_categorical(labels, 3)

print("Training model...")

model = create_hybrid_model()

model.fit(
    [images, numeric_features],
    labels,
    epochs=10,
    batch_size=16
)

model.save("trained_hybrid_model.h5")

print("Model saved successfully!")