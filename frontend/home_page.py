import streamlit as st
import requests

# Define your backend URL
backend_url = "http://api:8000"

# Page configuration
st.set_page_config(
    page_title='Sepsis Prediction',
    page_icon='💉',
    layout='wide'
)

st.title('Sepsis Input Features🩺')
st.markdown("""
Welcome to the Sepsis Prediction application 🚨. 
Sepsis is a serious condition in which the body responds improperly 
to an infection. The infection-fighting processes turn on the body, causing the organs to work poorly. Sepsis may progress to septic shock.
This is a dramatic drop in blood pressure that can damage the lungs, kidneys, liver, and other organs. When the damage is severe, it can lead to death.
Early treatment of sepsis improves chances for survival. 
This app allows the user to enter a patient's details and predict if the patient will test positive or negative for sepsis, thus allowing for early treatment.
To get more information and a description of the details, click [Go to Detail Definition Page](http://localhost:8501/detail_description_page).
Otherwise, please enter the patient's details in the form below to predict the likelihood of sepsis. 
""")

def show_form():
    st.header('Input Features 📖')
    with st.form('input-feature'):
        col1, col2, col3 = st.columns(3)
        with col1:
            PRG = st.number_input('PRG', min_value=0, step=1)
            PL = st.number_input('PL', min_value=0, step=1)
            PR = st.number_input('PR', min_value=0, step=1)
        with col2:
            SK = st.number_input('SK', min_value=0, step=1)
            TS = st.number_input('TS', min_value=0, step=1)
            M11 = st.number_input('M11', min_value=0, step=1)
        with col3:
            BD2 = st.number_input('BD2', min_value=0, step=1)
            Age = st.number_input('Age', min_value=21, step=1)
            Insurance = st.number_input('Insurance', min_value=0, max_value=1)
            
        submit_button = st.form_submit_button('Predict')
        
        if submit_button:
            input_data = {
                'PRG': PRG,
                'PL': PL,
                'PR': PR,
                'SK': SK,
                'TS': TS,
                'M11': M11,
                'BD2': BD2,
                'Age': Age,
                'Insurance': Insurance
            }
            
            try:
                response = requests.post(f"{backend_url}/predict_sepsis", json=input_data)
                response.raise_for_status()
                
                if response.status_code == 200:
                    prediction = response.json()['prediction']
                    st.session_state['prediction'] = prediction
                    st.session_state['message'] = f'The patient tested {prediction} for sepsis'
                    st.session_state['status'] = 'success'
                else:
                    st.session_state['message'] = f'Error: {response.json()["detail"]}'
                    st.session_state['status'] = 'error'
            except requests.exceptions.RequestException as e:
                st.session_state['message'] = f'Connection error: {e}'
                st.session_state['status'] = 'error'

if __name__ == '__main__':
    show_form()

    if 'message' in st.session_state:
        if st.session_state['status'] == 'success':
            st.success(st.session_state['message'])
        else:
            st.error(st.session_state['message'])
