import base64

import streamlit as st

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
