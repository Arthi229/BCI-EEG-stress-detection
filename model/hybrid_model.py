import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D, concatenate

def create_hybrid_model():

    # -------- Image Branch (CNN) --------
    image_input = Input(shape=(224, 224, 3))

    x = Conv2D(16, (3,3), activation='relu')(image_input)
    x = MaxPooling2D(2,2)(x)
    x = Conv2D(32, (3,3), activation='relu')(x)
    x = MaxPooling2D(2,2)(x)
    x = Flatten()(x)

    # -------- Numeric Branch --------
    numeric_input = Input(shape=(3,))
    y = Dense(16, activation='relu')(numeric_input)

    # -------- Fusion --------
    combined = concatenate([x, y])
    z = Dense(64, activation='relu')(combined)
    output = Dense(3, activation='softmax')(z)

    model = Model(inputs=[image_input, numeric_input], outputs=output)

    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model