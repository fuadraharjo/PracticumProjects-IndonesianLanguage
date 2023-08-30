
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.optimizers import Adam


def load_train(path):
    
    """
    Kode ini memuat bagian training set dari file path
    """
    
    # memuat path untuk data train dan label train
    face_path = path + 'final_files/'
    label_path = path + 'labels.csv'

    # memuat dataset label train
    labels = pd.read_csv(label_path)

    # memuat data train menggunakan ImageDataGenerator    
    train_datagen = ImageDataGenerator(rescale=1/255,validation_split=0.25)
    train_gen_flow = train_datagen.flow_from_dataframe(
        dataframe=labels,
        directory=face_path,
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        seed=12345)
    
    return train_gen_flow


def load_test(path):
    
    """
    Kode ini memuat bagian validation set/test set dari file path
    """
    
    # memuat path untuk data test dan label test
    face_path = path + 'final_files/'
    label_path = path + 'labels.csv'

    # memuat dataset label test
    labels = pd.read_csv(label_path)

    # memuat data test menggunakan ImageDataGenerator   
    test_datagen = ImageDataGenerator(rescale=1/255,validation_split=0.25)
    test_gen_flow = test_datagen.flow_from_dataframe(
        dataframe=labels,
        directory=face_path,
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        seed=12345)

    return test_gen_flow


def create_model(input_shape=(224,224,3)):
    
    """
    Kode ini mendefinisikan model
    """
    
    # rangkaian CNN
    resnet = ResNet50(input_shape=input_shape,
                 include_top=False,classes=1000,
                 weights='imagenet') 
    resnet.trainable = True
    model = Sequential()
    model.add(resnet)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(1, activation='relu')) 

    # optimizer dan metrik
    model.compile(
        optimizer=Adam(),
        loss='mean_squared_error',
        metrics=['mae'],
    )

    return model


def train_model(model, train_data, test_data, batch_size=None, epochs=20,
                steps_per_epoch=None, validation_steps=None):

    """
    Melatih model dengan parameter yang diberikan
    """
    
    # training dan validasi model CNN
    model.fit(train_data,
            validation_data=test_data,
            batch_size=batch_size,
            epochs=epochs,
            steps_per_epoch= len(train_data) if steps_per_epoch is None else steps_per_epoch,
            validation_steps= len(test_data) if validation_steps is None else validation_steps,
            verbose=2)

    return model


