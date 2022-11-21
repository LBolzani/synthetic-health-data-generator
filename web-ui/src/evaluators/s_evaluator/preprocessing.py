import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def get_encoded_df(df_or, df_sy):
    features = df_or.columns.to_list()
    df_encoded_or = df_or.copy()
    df_encoded_sy = df_sy.copy()

    label_encoders = {}
    df_dtypes = df_or.dtypes
    for feature in features:
        if df_dtypes[feature] == np.number:
            continue
        le = LabelEncoder()
        le.fit(df_or[feature])
        df_encoded_or[feature] = le.transform(df_or[feature])
        if feature in df_sy.columns:
            df_encoded_sy[feature] = le.transform(df_sy[feature])
        label_encoders[feature] = le

    return label_encoders, df_encoded_or, df_encoded_sy