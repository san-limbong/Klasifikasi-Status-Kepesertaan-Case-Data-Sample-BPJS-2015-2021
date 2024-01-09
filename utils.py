# utils.py
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Definisi columns_to_encode
columns_to_encode = ['PSTV02','PSTV04', 'PSTV05', 'PSTV06', 'PSTV07', 'PSTV08', 'PSTV09', 'PSTV10', 'PSTV11',
                     'PSTV12', 'PSTV13', 'PSTV14', 'PSTV15', 'PSTV16']

def label_encode_columns(dataframe, columns):
    le = LabelEncoder()
    for column in columns:
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            dataframe[column] = dataframe[column].astype(str)
        dataframe[column] = le.fit_transform(dataframe[column])
    return dataframe
