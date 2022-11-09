import streamlit as st

import streamlit as st
import os
import pathlib
from os import listdir
from os.path import isfile, join
from sdv.tabular import GaussianCopula
from sdv.evaluation import evaluate


import sys, os
setupBaseDir = os.path.dirname(__file__)
sys.path.insert(0, setupBaseDir)

real_dir = os.path.join(setupBaseDir, "../data/single_table/real/")
model_TVAE_dir = os.path.join(setupBaseDir, "../data/single_table/models/TVAE/")
model_CopulaGAN_dir = os.path.join(setupBaseDir, "../data/single_table/models/CopulaGAN/")
model_CTGAN_dir = os.path.join(setupBaseDir, "../data/single_table/models/CTGAN/")
model_GaussianCopula_dir = os.path.join(setupBaseDir, "../data/single_table/models/GaussianCopula/")
model_TabularPreset_dir = os.path.join(setupBaseDir, "../data/single_table/models/TabularPreset/")

st.write("""
# SYNTHETIC MODEL EVALUATOR
""")
#Add sidebar
with st.form(key ='Form1'):
    with st.sidebar:
        parent_path = pathlib.Path(__file__).parent.parent.resolve()
        model_path = model_TVAE_dir
        onlyfiles = [f for f in listdir(model_path) if isfile(join(model_path, f))]
        option6 = st.selectbox('Pick or paste your Model ID .pkl', onlyfiles)    
        data_type = st.sidebar.radio('Data Format', ('SingleTable', 'MultiTable'))
        num_of_tweets = st.sidebar.number_input('Number of rows to evaluate with', 100)
        submitted1 = st.form_submit_button(label = 'Evaluate Model')
        #model = GaussianCopula.load(option6)

#option1 = st.selectbox( 'What industry would you like to see data for?', ("Biology", "clinical_patient_histories"))
#option7 = st.sidebar.selectbox('Model ID:', ("Biology", "clinical_patient_histories"))


# st.selectbox(
# if st.button('Run Model'):
#     st.write('Why hello there')
# file_location=model_path
# st.write(file_location))
# use `file_location` as a parameter to the main script