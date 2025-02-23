import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Defina o caminho para o seu dataset.
# O dataset deve estar organizado com uma pasta para cada classe (pessoa).
# Exemplo: dataset_faces/Pessoa1, dataset_faces/Pessoa2, ...
dataset_path = 'dataset_faces'

# Parâmetros de entrada
img_height, img_width = 160, 160
batch_size = 32

# Criação de geradores de dados com data augmentation
train_datagen = ImageDataGenerator(
    rescale=1.0/255,
    validation_split=0.2,  # 20% dos dados para validação
    rotation_range=10,
    zoom_range=0.2,
    horizontal_flip=True
)

train_generator = train_datagen.flow_from_directory(
    dataset_path,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    dataset_path,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Construção de uma CNN simples
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(train_generator.num_classes, activation='softmax')
])

# Compilação do modelo
model.compile(
    optimizer=Adam(learning_rate=1e-4),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Exibir a arquitetura do modelo
model.summary()

# Treinamento do modelo
epochs = 25  # ajuste o número de épocas conforme necessário
history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)

# Salvar o modelo treinado para uso posterior
model.save("face_classifier.h5")
