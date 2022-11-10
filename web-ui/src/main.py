import pandas as pd
import streamlit as st
import constants.evaluatorsFnsName as evalFN

from s_evaluator.evaluator import Evaluator
from synth_generator.algorithms import ctan, copulaGan, gaussianCopula, tvae, algos
from synth_generator.ComparisonModels import ComparisonModels

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; margin-bottom: 10px;margin-top: 10px;'>Synthetic data generator tool</h1>",
            unsafe_allow_html=True)

col1, col2 = st.columns([6,15], gap="medium")

st.session_state.gen_synth_data = False
st.session_state.gen_eval_model = False

@st.cache(allow_output_mutation=True)
def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

@st.cache
def compute_syntData(df_real_data, algorithm, parameters):
    compareModel = ComparisonModels(df_real_data, algos[algorithm], parameters)
    return compareModel.GenerateSynth(parameters)


with col1:
    st.subheader("Settings")
    st.file_uploader("Upload data:", key='upload_file')

    algorithm = st.selectbox('Algorithm:',(ctan, copulaGan, gaussianCopula,tvae), key= 'algorithm_gen')
    parameters = st.selectbox('Parameters:', ('gaussian', 'gamma', 'beta', 'student_t', 'gaussian_kde', 'truncated_gaussian'), key= 'param_gen')

    evaluators_algo = st.radio('Evaluators:',
                               (evalFN.PCA, evalFN.SVD, evalFN.RANDOM_FOREST,
                                evalFN.LINEAR_REG, evalFN.CLASSIFICATION, evalFN.REAL_VS_SYNTH),
                               key='algo_eval')

    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button('Generate'):
        if st.session_state.upload_file is not None:
            st.session_state.gen_synth_data = True
        else:
            st.session_state.gen_synth_data = False
            st.error("Please upload a file")


with col2:
    st.subheader("Analysis")
    tab1, tab2 = st.tabs(["🗃 Data", "📈 Chart"])
    if st.session_state.upload_file is not None and st.session_state.gen_synth_data:
        df_real_data = load_data(st.session_state.upload_file)
        df_synth_data, score = compute_syntData(df_real_data, st.session_state.algorithm_gen,
                                                st.session_state.param_gen)

    with tab1:
        if st.session_state.upload_file is not None and st.session_state.gen_synth_data:
            if score is not None and df_synth_data is not None:
                st.write("Score: {}".format(score))
                st.dataframe(df_synth_data)
        else:
            st.info("Upload a file in 'Settings' to have your synthetic data!")

    with tab2:
        if st.session_state.upload_file is not None and st.session_state.gen_synth_data:
            evaluator = Evaluator(df_real_data, df_synth_data, df_real_data['diagnosis'])
            evaluator.preprocess()
            evaluator.do_clustering()
            if st.session_state.algo_eval == evalFN.PCA:
                st.pyplot(evaluator.plot_pca())
            elif st.session_state.algo_eval == evalFN.SVD:
                st.pyplot(evaluator.plot_svd())
            elif st.session_state.algo_eval == evalFN.RANDOM_FOREST:
                st.pyplot(evaluator.plot_random_forest())
            elif st.session_state.algo_eval == evalFN.CLASSIFICATION:
                st.pyplot(evaluator.plot_correlation())
            else:
                st.pyplot(evaluator.plot_pca())
        else:
            st.info("Upload a file in 'Settings' to have your synthetic data!")
