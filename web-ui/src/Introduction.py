# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title('Uber pickups in NYC')

# DATE_COLUMN = 'date/time'
# #DATA_URL = ('https://s3-us-west-2.amazonaws.com/''streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache
# def load_data(file_path, nrows):
#     data = pd.read_csv(file_path, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data


# uploaded_file = st.file_uploader("Choose a file")

# if uploaded_file is not None:
#     data_load_state = st.text('Loading data...')
#     data = load_data(uploaded_file, 10000)
#     data_load_state.text("Done! (using st.cache)")

#     if st.checkbox('Show raw data'):
#         st.subheader('Raw data')
#         st.write(data)

#     st.subheader('Number of pickups by hour')
#     hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#     st.bar_chart(hist_values)

#     # Some number in the range 0-23
#     #hour_to_filter = st.slider('hour', 0, 23, 17)
#     #filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

#     #st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#     #st.map(filtered_data)

import streamlit as st

# #Generations page
# st.markdown('Generations')
# st.sidebar.markdown('Generations')

# #Evaluations Page
# st.markdown('Evaluations')
# st.sidebar.markdown('Evaluations')

# #Benchmarking Page
# st.markdown('Benchmarking')
# st.sidebar.markdown('Benchmarking')


def navbar_component():
    with open("assets/images/settings.png", "rb") as image_file:
        image_as_base64 = base64.b64encode(image_file.read())

    navbar_items = ''
    for key, value in NAVBAR_PATHS.items():
        navbar_items += (f'<a class="navitem" href="/?nav={value}">{key}</a>')

    settings_items = ''
    for key, value in SETTINGS.items():
        settings_items += (
            f'<a href="/?nav={value}" class="settingsNav">{key}</a>')

    component = rf'''
            ....
    '''
    st.markdown(component, unsafe_allow_html=True)
    
    js = '''
    <script>
    ....
    </script>
    '''
    html(js)

#st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
st.write('''
# SDV SYNTHETIC MODEL AND DATA STORE
''')
st.write('This is an app to accept real data and generate a FAST_ML,GaussianCopula, CTGAN, CopulaGAN or TVAE model based on the data and a synthetic dataset')
st.write('1. Start by generating some data saving the hash key for your dataset, to use it to generate the sample data')
st.write('2. Check the evaluation of your model on the evaluations tab')
st.write('3. Benchmark your model using the Benchmarking tool')
