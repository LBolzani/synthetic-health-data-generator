import streamlit as st
import os.path
import pathlib, string
import pandas as pd 
import numpy as np 
from hashlib import md5
from time import localtime
import time
import sys, os
setupBaseDir = os.path.dirname(__file__)
sys.path.insert(0, setupBaseDir)
import string
from sdv.lite import TabularPreset
import hydralit as hy
from sdv.tabular import GaussianCopula, CTGAN, CopulaGAN, TVAE
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
from scipy.stats import kstest
from sdv.evaluation import evaluate
import mitosheet
import glob
import random
from sdv import Metadata

#session state management
if 'prefix' not in st.session_state:
    st.session_state.prefix = md5(str(localtime()).encode('utf-8')).hexdigest()

#specifying directories
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

#check if files already exist
synthetic_TVAE_path = synthetic_TVAE_dir+st.session_state.prefix+'.csv'
synthetic_CopulaGAN_path = synthetic_CopulaGAN_dir+st.session_state.prefix+'.csv'
synthetic_CTGAN_path = synthetic_CTGAN_dir+st.session_state.prefix+'.csv'
synthetic_TabularPreset_path = synthetic_TabularPreset_dir+st.session_state.prefix+'.csv'
synthetic_GaussianCopula_path = synthetic_GaussianCopula_dir+st.session_state.prefix+'.csv'

#check if files already exist
model_TVAE_path = model_TVAE_dir+st.session_state.prefix+'.pkl'
model_CopulaGAN_path = model_CopulaGAN_dir+st.session_state.prefix+'.pkl'
model_CTGAN_path = model_CTGAN_dir+st.session_state.prefix+'.pkl'
model_GaussianCopula_path = model_GaussianCopula_dir+st.session_state.prefix+'.pkl'
model_TabularPreset_path = model_TabularPreset_dir+st.session_state.prefix+'.pkl'

#Begin
st.write("""
# SYNTHETIC DATA AND MODEL GENERATOR
""")
option3 = st.sidebar.selectbox('What type of data do you have?', ("singleCSVTable", "multipleCSVTables"))
#option4 = st.sidebar.selectbox('which model would you like to use?', ("TabularPreset","GaussianCopula", "CTGAN", "CopulaGAN", "TVAE"))
#option1 = st.selectbox( 'What type of data do you have?', ("singleCSVTable", "multipleCSVTables"))
#ption2 = st.selectbox( 'which model would you like to use?', ("TabularPreset","GaussianCopula", "CTGAN", "CopulaGAN", "TVAE"))

st.write('Model ID:')
st.write(st.session_state.prefix)

tab1, tab2, tab3 = st.tabs(["Real Data", "Generate Data", "Evaluations"])

with tab1:
    if option3 == 'singleCSVTable':
        real_dir = os.path.join(setupBaseDir, "../data/single_table/real/")
        uploaded_files = st.file_uploader("Choose a file")
        dataframe = pd.read_csv(uploaded_files)

        #check if file exists
        real_path = real_dir+st.session_state.prefix+'.csv'
        isExist = os.path.exists(real_path)
        if isExist == True:
            os.remove(real_path)

        #save real file
        dataframe.to_csv(real_dir+st.session_state.prefix+'.csv', sep=',' ) 
        st.write(real_dir+st.session_state.prefix+'.csv')


        st.write('Generate synthetic data based on the uploaded dataset in the generate data tab')
    else:
        
        uploaded_files = st.file_uploader("Choose CSV files", accept_multiple_files=True)
        
        dataframe_collection = {}

        counter = 1
        if uploaded_files == None:
            st.write('Generate synthetic data based on the uploaded dataset on the generate data tab')
        else:
            for uploaded_file in uploaded_files:
                dataframe = pd.read_csv(uploaded_file)
                dataframe_collection[counter] = dataframe
                st.write(real_multi_dir+st.session_state.prefix+'_'+str(counter)+'.csv')
                dataframe.to_csv(real_multi_dir+st.session_state.prefix+'_'+str(counter)+'.csv', sep=',' )
                dataframe = dataframe.append(dataframe_collection, ignore_index=True)
                st.write(dataframe)
                counter = counter + 1
        
        
            # bytes_data = uploaded_file.read()
            # st.write("filename:",complete_name)
            # st.write(bytes_data)
            
            #bytes_data = uploaded_file.read()
            #st.write("filename:", uploaded_file.name)
            #st.write(bytes_data)

    # if uploaded_files:
    #     for file in uploaded_files:
    #         file.seek(0)
    #     uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    #     raw_data = pd.concat(uploaded_data_read)
    #     raw_data.head()
    #     st.snow()
    # label = 'This'
    # uploaded_file = st.file_uploader(label,accept_multiple_files=True )
    # if uploaded_file is not None:
    #     #df = pd.read_csv(uploaded_file.getvalue())
    #     bytes_data = uploaded_file.getvalue()
    #     data = uploaded_file.getvalue().decode('utf-8').splitlines()         
    #     st.session_state["preview"] = ''
    #     for i in range(0, min(5, len(data))):
    #         st.session_state["preview"] += data[i]
    #     #st.session_state["preview"] += df.info()

    # preview = st.text_area("Metadata", "", height=150, key="preview")
    # upload_state = st.text_area("State", "", key="upload_state")
    # def upload():
    #     if uploaded_file is None:
    #         st.session_state["State"] = "Upload a file first!"
    #     else:
    #         data = uploaded_file.getvalue().decode('utf-8')
    #         parent_path = pathlib.Path(__file__).parent.parent.resolve()           
    #         save_path = os.path.join(parent_path, "data")
    #         complete_name = os.path.join(save_path, f"{prefix}_{uploaded_file.name}")
    #         destination_file = open(complete_name, "w")
    #         destination_file.write(data)
    #         destination_file.close()
    #         st.session_state["state"] = "Saved " + complete_name + " successfully!"
    #         return complete_name
    # st.button("Upload file to Sandbox", on_click=upload)



with tab2:
    if option3 == 'singleCSVTable':
        #Handle different models
        sample_size = st.number_input('Rows', min_value=1, max_value=100000, value=5, step=1)

        #reading current file(s)
        df = pd.read_csv(real_dir+st.session_state.prefix+'.csv')



        model_paths = ['model_TVAE_path', 'model_CopulaGAN_path', 'model_CTGAN_path','model_GaussianCopula_path', 'model_TabularPreset_path']

        for model_path in model_paths:
            isExist = os.path.exists(model_path)
            if isExist == True:
                os.remove(model_path)


        #specify fit and save model
        #1. Tabular Preset
        TabularPreset_model = TabularPreset(name='FAST_ML', metadata=df.info())
        TabularPreset_model.fit(df)
        TabularPreset_model.save(model_TabularPreset_path)

        #2. CopulaGAN
        CopulaGAN_model = CopulaGAN()
        CopulaGAN_model.fit(df)
        CopulaGAN_model.save(model_CopulaGAN_path)

        #3. CTGAN
        CTGAN_model = CTGAN()
        data=df
        CTGAN_model.fit(data)
        CTGAN_model.save(model_CTGAN_path)

        #4. GaussianCopula
        GaussianCopula_model = GaussianCopula()
        GaussianCopula_model.fit(df)
        GaussianCopula_model.save(model_GaussianCopula_path)

        #5. TVAE
        TVAE_model = GaussianCopula()
        TVAE_model.fit(df)
        TVAE_model.save(model_TVAE_path)

        #Generate Datasets
        if st.button('Generate'):
            with st.spinner('Wait for it...'):
                time.sleep(5) 
                #TVAE_synthetic_data = model.sample(num_rows=sample_size)

                model_paths = [synthetic_TVAE_path, synthetic_CopulaGAN_path, synthetic_CTGAN_path,synthetic_TabularPreset_path,synthetic_GaussianCopula_path ]
                for model_path in model_paths:
                    isExist = os.path.exists(model_path )
                    if isExist == True:
                        os.remove(model_path)
                
                #save synthetic data
                #1. Tabular Preset
                TabularPreset_model.sample(num_rows=sample_size, output_file_path=synthetic_TabularPreset_path)
                #2. TVAE
                TVAE_model.sample(num_rows=sample_size, output_file_path=synthetic_TVAE_path)
                #3. CTGAN 
                CTGAN_model.sample(num_rows=sample_size, output_file_path=synthetic_CTGAN_path)
                #4. GaussianCopula_model
                GaussianCopula_model.sample(num_rows=sample_size, output_file_path=synthetic_GaussianCopula_path)
                #5. CopulaGAN
                CopulaGAN_model.sample(num_rows=sample_size, output_file_path=synthetic_CopulaGAN_path)
                #TabularPresetReport = QualityReport()

                #displaying previews
                #1. TabularPreset
                st.write('Tabular Preset Sample:')
                st.write(TabularPreset_model.sample(num_rows=sample_size))
                st.success('Done!')

                #Download Button
                df_TabularPreset = pd.read_csv(synthetic_TabularPreset_path)
                def convert_df(df_TabularPreset):
                    # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return dataframe.to_csv().encode('utf-8')

                csv = convert_df(df_TabularPreset)
                st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name=synthetic_TabularPreset_path+st.session_state.prefix+'.csv',
                mime='text/csv')

                #2. CopulaGAN
                st.write('CopulaGAN Sample:')
                st.write(CopulaGAN_model.sample(num_rows=sample_size))
                st.success('Done!')
                
                df_CopulaGAN = pd.read_csv(synthetic_CopulaGAN_path)
                def convert_df(df_CopulaGAN):
                    # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return df_CopulaGAN.to_csv().encode('utf-8')

                csv = convert_df(df_CopulaGAN)
                st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name=synthetic_CopulaGAN_path+st.session_state.prefix+'.csv',
                mime='text/csv')

                #3. GaussianCopula
                st.write('GaussianCopula Sample:')
                st.write(GaussianCopula_model.sample(num_rows=sample_size))
                st.success('Done!')
                
                df_GaussianCopula = pd.read_csv(synthetic_GaussianCopula_path)
                def convert_df(df_GaussianCopula):
                    # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return df_GaussianCopula.to_csv().encode('utf-8')

                csv = convert_df(df_GaussianCopula)
                st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name=synthetic_GaussianCopula_path+st.session_state.prefix+'.csv',
                mime='text/csv')

                #4. CTGAN
                st.write('CTGAN Sample:')
                st.write(CTGAN_model.sample(num_rows=sample_size))
                st.success('Done!')
                
                df_CTGAN = pd.read_csv(synthetic_CTGAN_path)
                def convert_df(df_CTGAN):
                    # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return df.to_csv().encode('utf-8')

                csv = convert_df(df_CTGAN)

                st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name=synthetic_CTGAN_path+st.session_state.prefix+'.csv',
                mime='text/csv')


                #5. TVAE
                st.write('TVAE Sample:')
                st.write(TVAE_model.sample(num_rows=sample_size))
                st.success('Done!')

                
                df_TVAE = pd.read_csv(synthetic_TVAE_path)
                def convert_df(df_TVAE):
                    # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return df.to_csv().encode('utf-8')

                csv = convert_df(df_TVAE)

                st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name=synthetic_TVAE_path+st.session_state.prefix+'.csv',
                mime='text/csv')


                # st.download_button(
                # label="Download data as Zip File",
                # data = csv,
                # file_name=st.session_state.prefix+'.csv',
                # mime='text/csv',)
    else:
        #Ask for sample size
        sample_size = st.text_input('Enter the number of rows of synthetic data you want to generate',5)
        #saving links for real and synthetic data and models
        #a)real data

        counter = 0

        #file_list = [filename for filename in os.listdir(real_multi_dir) if filename.startswith(st.session_state.prefix)]
        
        file_count = len([filename for filename in os.listdir(real_multi_dir) if filename.startswith(st.session_state.prefix)])
        
        dfs = []
        file_names = []
        #Generating real dataframes
        #listing file names
        col1, col2 = st.columns(2)
        with col1:
            for i in range(file_count):
                multi_file=real_multi_dir+st.session_state.prefix+'_'+str(i+1)+'.csv'
                df = pd.read_csv(multi_file)
                #file_names.append(multi_file)
                #primary_key = st.selectbox('which column is the primary key?', (df.columns))
                #st.write(df.columns)
                keys = random.sample(range(1000, 9999), len(df.columns))
                primary_key = st.selectbox('Which column is the primary key for table:'+str(i+1),( df.columns), key=keys[i])
                #append dataframes for later use
                dfs.append(df)

        with col2:
            txt = st.text_area( 'Paste here metadata.json')
            st.write(dfs)

        if st.button('Generate Synthetic Data'):
            st.write('Why hello there')


            #st.write(file_names)
            

            #extracting dataframes


        












        #st.write(df)

        #b)synthetic data by model


        #c) models

        #save the dataframes


        #Ask for related columns




with tab3:
    if option3 == 'singleCSVTable':
        #Distribution of the real data:
        st.write('Distribution of real data')
        df_real = pd.read_csv(real_dir+st.session_state.prefix+'.csv')
        np_real = df_real.to_numpy()
        np_real = np.random.normal(1, 1, size=50)
        fig, ax = plt.subplots()
        ax.hist(np_real, bins=20)
        st.pyplot(fig)

        #Distribution of the Tabular Preset data:
        st.write('Distribution of TabularPreset data')
        df_TabularPreset = pd.read_csv(synthetic_TabularPreset_path)
        np_TabularPreset = df_TabularPreset.to_numpy()
        np_TabularPreset = np.random.normal(1, 1, size=50)
        fig, ax = plt.subplots()
        ax.hist(np_TabularPreset, bins=20)
        st.pyplot(fig)
        

        #Distribution of the TVAE data:
        st.write('Distribution of TVAE data')
        df_TVAE = pd.read_csv(synthetic_TVAE_path)
        np_TVAE = df_TVAE.to_numpy()
        np_TVAE = np.random.normal(1, 1, size=50)
        fig, ax = plt.subplots()
        ax.hist(np_TVAE, bins=20)
        st.pyplot(fig)

        #Distribution of the GaussianCopula  data:
        st.write('Distribution of GaussianCopula data')
        df_GaussianCopula = pd.read_csv(synthetic_GaussianCopula_path)
        np_GaussianCopula = df_GaussianCopula.to_numpy()
        np_GaussianCopula = np.random.normal(1, 1, size=50)
        fig, ax = plt.subplots()
        ax.hist(np_GaussianCopula, bins=20)
        st.pyplot(fig)

        #Score of the CTGAN  data:
        st.write('Distribution of CTGAN data')
        df_CTGAN = pd.read_csv(synthetic_CTGAN_path)
        np_CTGAN = df_CTGAN.to_numpy()
        np_CTGAN = np.random.normal(1, 1, size=50)
        fig, ax = plt.subplots()
        ax.hist(np_CTGAN, bins=20)
        st.pyplot(fig)

        #Score of the CopulaGAN  data:

        st.write('Distribution of CopulaGAN data')
        df_CopulaGAN = pd.read_csv(synthetic_CopulaGAN_path)
        np_CopulaGAN = df_CopulaGAN.to_numpy()
        np_CopulaGAN = np.random.normal(1, 1, size=50)
        fig, ax = plt.subplots()
        ax.hist(np_CopulaGAN, bins=20)
        st.pyplot(fig)
    else:
        st.write('Generate something')


