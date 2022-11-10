from s_evaluator import evaluator
import pandas as pd
import streamlit as st

import os



st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Synthetic data tool</h1>", unsafe_allow_html=True)

base_file = os.path.join(os.path.dirname(__file__), '../../evaluators/')


df_real_data = pd.read_csv(base_file + "test/resources/data/breast_cancer_df.csv")
df_synth_data = pd.read_csv(base_file + "test/resources/data/SyntheticModels/CopulaGAN_beta.csv")

output = df_real_data["diagnosis"]

evaluator = evaluator.Evaluator(df_real_data, df_synth_data, output)
evaluator.preprocess()
evaluator.do_clustering()


st.markdown("<h2 style='text-align: center;'>PCA</h2>", unsafe_allow_html=True)
fig = evaluator.plot_pca()
st.pyplot(fig)

st.markdown("<h2 style='text-align: center;'>SVD</h2>", unsafe_allow_html=True)
fig = evaluator.plot_svd()
st.pyplot(fig)

st.markdown("<h2 style='text-align: center;'>Random Forest</h2>", unsafe_allow_html=True)
fig = evaluator.plot_random_forest()
st.pyplot(fig)

st.markdown("<h2 style='text-align: center;'>Correlation</h2>", unsafe_allow_html=True)
fig = evaluator.plot_correlation()
st.pyplot(fig)
