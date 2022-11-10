import pandas as pd
import streamlit as st

from s_evaluator.evaluator import Evaluator

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Synthetic data tool</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([6,12,6], gap="medium")
upload_file = None
figure = None
df_synth_data = None

with col1:
    st.subheader("Generate")
    uploaded_file = st.file_uploader("Upload data")
    algorithm = st.selectbox('Algorithm',('CTGAN', 'CopulaGAN', 'GaussianCopula','TVAE'))
    parameters = st.selectbox('Parameters', ('Gaussian', 'Gamma', 'Beta', 'Student_t', 'Gaussian_Kde', 'Trunc_Gaussian'))
    if st.button('Generate'):
        if uploaded_file is not None:
            st.write('Gen start')
        else:
            st.error("Please upload a file")


with col2:
    st.subheader("Analysis")
    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
    with tab1:
        #tab1.subheader("A tab with a chart")
        if figure is not  None:
            st.pyplot(figure)

    with tab2:
        if df_synth_data is not None:
            st.dataframe(df_synth_data)


        if st.button('Download'):
            st.write('Download start')


with col3:
    st.subheader("Evaluation")
    evaluators_algo = st.radio('Evaluators',
                               ('PCA', 'SVD', 'Randomforest', 'Linear Regression', 'Classification', 'Real vs Synth Data'))

    if st.button('Evaluate'):
        if uploaded_file is not None:
            df_real_data = pd.read_csv(uploaded_file)
            df_synth_data = pd.read_csv("/Users/luca.bolzani/Downloads/SyntheticModels/CopulaGAN_beta.csv")
            evaluator = Evaluator(df_real_data, df_synth_data, df_real_data['diagnosis'])
            evaluator.preprocess()
            evaluator.do_clustering()

            if evaluators_algo == 'PCA':
                figure = evaluator.plot_pca()

        else:
            st.error("Please upload a file")






