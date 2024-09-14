from argparse import ArgumentParser

import matplotlib.pyplot as plt

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import plot_model

classes = ['acrochordon', 'actinic_keratosis', 'angiofibroma_or_fibrous_papule',
           'angiokeratoma', 'angioma', 'atypical_spitz_tumor', 'basal_cell_carcinoma'
           'cafe_au_lait_macule', 'clear_cell_acanthoma', 'dermatofibroma',
           'lentigo_nos', 'lentigo_simplex', 'lichenoid_keratosis', 'melanoma',
           'melanoma_metastasis', 'neurofibroma', 'nevus', 'nevus_spilus',
           'other', 'pigmented_benign_keratosis', 'pyogenic_granuloma', 'scar',
           'sebaceous_adenoma', 'sebaceous_hyperplasia', 'seborrheic_keratosis',
           'solar_lentigo', 'squamous_cell_carcinoma', 'vascular_lesion', 'verruca']