import streamlit as st

import streamlit as st
import os
import pathlib
from os import listdir
from os.path import isfile, join
from sdv.tabular import GaussianCopula
from sdv.evaluation import evaluate

#Performance imports
from sdv import load_demo, SDV
from sdv.tabular import CTGAN, CopulaGAN
from sdv.evaluation import evaluate


import pandas as pd
import numpy as np
import sys

from sklearn.cluster import KMeans, FeatureAgglomeration

from sklearn.decomposition import PCA, NMF, TruncatedSVD
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

from scipy.stats import zscore

font = {'size'   :      14}

matplotlib.rc('font', **font)

import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 100

sns.set(rc={"figure.dpi":100, 'savefig.dpi':300})
sns.set_theme(style='whitegrid')

random_seed = 31415926

np.random.seed(random_seed)

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

#other imports
import sys, os
setupBaseDir = os.path.dirname(__file__)
sys.path.insert(0, setupBaseDir)

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

st.write("""
# SYNTHETIC MODEL EVALUATOR
""")
#Begin
parent_path = pathlib.Path(__file__).parent.parent.resolve()
model_path = model_TVAE_dir
onlyfiles = [f for f in listdir(model_path) if isfile(join(model_path, f))]

    
tab1, tab2, tab3 = st.tabs(['Performance','2','3'])
with tab1:
    data_type = st.sidebar.radio('Data Format', ('SingleTable', 'MultiTable'))
    if data_type == 'MultiTable':
        st.write('Future Implementation')
    else:
        option6 = st.selectbox('Pick or paste your Model ID (hash) .pkl', onlyfiles)    
        sample_size = st.number_input('Number of rows to evaluate with', 100)
        if st.button('Evaluate'):
            st.write('Why hello there')
        






        #model = GaussianCopula.load(option6)

#option1 = st.selectbox( 'What industry would you like to see data for?', ("Biology", "clinical_patient_histories"))
#option7 = st.sidebar.selectbox('Model ID:', ("Biology", "clinical_patient_histories"))


# st.selectbox(
# if st.button('Run Model'):
#     st.write('Why hello there')
# file_location=model_path
# st.write(file_location))
# use `file_location` as a parameter to the main script