import streamlit as st
st.set_page_config(
    page_title='Sepsis Prediction',
    page_icon='',
    layout='wide'
)

st.title('Sepsis detail desription page ')
st.markdown("""

Welcome to the Sepsis detail description page.
Below is a table showing the details about a patient and their descriptions.

#### Details Definitions:
| Detail  | Description |
|-------------|-------------|
| PRG         | Plasma glucose |
| PL          | Blood Work Result-1 (mu U/ml) |
| PR          | Blood Pressure (mm Hg) |
| SK          | Blood Work Result-2 (mm) |
| TS          | Blood Work Result-3 (mu U/ml) |
| M11         | Body mass index (weight in kg/(height in m)^2) |
| BD2         | Blood Work Result-4 (mu U/ml) |
| Age         | Patient's age (years) |
| Insurance   | If a patient holds a valid insurance card |
| Sepsis      | Positive: if a patient in ICU will develop sepsis, and Negative: otherwise |
""")
