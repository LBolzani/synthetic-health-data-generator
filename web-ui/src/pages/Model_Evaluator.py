import streamlit as st
from os import path
import streamlit as st
import os
import pathlib
from os import listdir
from os.path import isfile, join
from sdv.tabular import GaussianCopula
from sdv.evaluation import evaluate
from table_evaluator import TableEvaluator
import time

#Performance imports

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib



#other imports
import sys, os
setupBaseDir = os.path.dirname(__file__)
sys.path.insert(0, setupBaseDir)

model_root = os.path.join(setupBaseDir, "../data/single_table/models/")
real_data_root = os.path.join(setupBaseDir, "../data/single_table/real/")
synthetic_data_root = os.path.join(setupBaseDir, "../data/single_table/synthetic/")
real_dir = os.path.join(setupBaseDir, "../data/single_table/real/")
real_multi_dir = os.path.join(setupBaseDir, "../data/multi_table/real/")
model_TVAE_dir = os.path.join(setupBaseDir, "../data/single_table/models/TVAE/")
model_CopulaGAN_dir = os.path.join(setupBaseDir, "../data/single_table/models/CopulaGAN/")
model_CTGAN_dir = os.path.join(setupBaseDir, "../data/single_table/models/CTGAN/")
model_GaussianCopula_dir = os.path.join(setupBaseDir, "../data/single_table/models/GaussianCopula/")
model_TabularPreset_dir = os.path.join(setupBaseDir, "../data/single_table/models/TabularPreset/")
synthetic_TVAE_dir = os.path.join(setupBaseDir, "../data/single_table/synthetic/TVAE/")
synthetic_CopulaGAN_dir = os.path.join(setupBaseDir, "../data/single_table/synthetic/CopulaGAN/")
synthetic_CTGAN_dir = os.path.join(setupBaseDir, "../data/single_table/synthetic/CTGAN/")
synthetic_GaussianCopula_dir = os.path.join(setupBaseDir, "../data/single_table/synthetic/GaussianCopula/")
synthetic_TabularPreset_dir = os.path.join(setupBaseDir, "../data/single_table/synthetic/TabularPreset/")

data_dirs = [real_dir, real_multi_dir, model_TVAE_dir, model_CopulaGAN_dir, model_CTGAN_dir, model_GaussianCopula_dir, model_TabularPreset_dir,synthetic_TVAE_dir, synthetic_CopulaGAN_dir,synthetic_CTGAN_dir, synthetic_GaussianCopula_dir,synthetic_TabularPreset_dir  ]

for dir in data_dirs:
    if not os.path.exists(dir):
        os.makedirs(dir)

#globals
option6 = []
available_models = []
model_list = ['TVAE', 'CopulaGAN', 'CTGAN', 'GaussianCopula','TabularPreset']

st.write("""
# SYNTHETIC MODEL EVALUATOR
""")
#Begin
parent_path = pathlib.Path(__file__).parent.parent.resolve()
model_path = model_TVAE_dir
onlyfiles = [f for f in listdir(model_path) if isfile(join(model_path, f))]

    
tab1, tab2, tab3, tab4 = st.tabs(['Performance','Correlations','Cumulative Sums Per Feature', 'LogisticRegression'])
data_type = st.sidebar.radio('Data Format', ('SingleTable', 'MultiTable'))
with tab1:
    if data_type == 'MultiTable':
        st.write('Future Implementation')
    else:
         option6 = st.selectbox('Pick or paste your Model ID (hash) .pkl', onlyfiles)    
         sample_size = st.number_input('Number of rows to evaluate with', 100)
         if st.button('Evaluate'):
            real_file = real_data_root+option6[:33]+'csv'
            real_data = pd.read_csv(real_file)
            #data = real_data.dropna(how='all', axis=1)
            with st.spinner('Evaluating...'):
                    time.sleep(5)
            st.success('Done! Proceed to the next tabs to view')

with tab2:
    if data_type == 'MultiTable':
        st.write('Future Implementation')
    else:
        col1,col2=st.columns(2)
        with col1:
            for model in model_list:
                if path.isfile(model_root+model+'/'+option6):
                    available_models.append(model)
                    #st.write(model)

            for model in available_models:
                #Getting real and synthetic files as dfs and plotting them
                synthetic_data = pd.read_csv(synthetic_data_root+model+'/'+option6[:33]+'csv')
                st.write('Correlation plot for '+model+' synthetic data')
                fig, ax = plt.subplots()
                sns.heatmap(synthetic_data.corr(), ax=ax)
                st.write(fig)
        with col2:
            st.write(option6)
                


            





