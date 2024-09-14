import pandas as pd
import numpy as np
import os
import shutil

from PIL import Image

from model.utils import *



def storage_data(file: np.ndarray, classification: str):
    r, g, b = np.split(file, 3, axis = 2)
    r = r.reshape(-1)
    g = g.reshape(-1)
    b = b.reshape(-1)

    bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], 
    zip(r,g,b)))
    bitmap = np.array(bitmap).reshape([file.shape[0], file.shape[1]])
    bitmap = np.dot((bitmap > 128).astype(float),255)
    len1 = len(bitmap[0])
    for i, row in enumerate(bitmap):
        if len(row) != len1:
            print(f'Problem in row: {i}')


def load_data(path: str, k: int) -> pd.DataFrame:
    walk = os.walk(path)
    path_train = './Data/Train'
    path_test = './Data/Test'
    for dirpath, _, filenames in walk:
        
        classification = get_last_name(dirpath)
        
        for i, name in enumerate(filenames):
            i_path = dirpath + '\\' + name
            image = Image.open(i_path)
            ary = np.array(image)

            storage_data(ary, classification)


