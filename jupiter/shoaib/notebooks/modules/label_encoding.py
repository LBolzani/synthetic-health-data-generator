import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def get_encoded_df(df):
    
    features = df.columns.to_list()
    df_encoded = df.copy()

    label_encoders = {}
    df_dtypes = df.dtypes 
    for feature in features:
        if df_dtypes[feature] == np.number:
            continue
        le = LabelEncoder()
        df_encoded[feature] = le.fit_transform(df[feature])
        label_encoders[feature] = le

    input_features = features[1:]
    output_feature = features[0]
    n_features = len(input_features)
    
    return label_encoders, df_encoded