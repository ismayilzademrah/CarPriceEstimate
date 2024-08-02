import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Faylları yükləyirik
brands = joblib.load('brands.pkl')
encoded_brand = joblib.load('encoded_brand.pkl')
encoded_model = joblib.load('encoded_model.pkl')
model = joblib.load('model.pkl')

# Streamlit tətbiqinin başlığı
st.title('Car Price Estimate App')

# 1. Year seçimi
current_year = datetime.now().year
year = st.sidebar.number_input('Year', min_value=1950, max_value=current_year, value=current_year, key='year_input')

# 2. Type seçimi
types = brands['type'].unique()
selected_type = st.sidebar.selectbox('Type', options=types, key='type_select')

# 3. Brand seçimi
brands_for_type = brands[brands['type'] == selected_type]['brand'].unique()
selected_brand = st.sidebar.selectbox('Brand', options=['...'] + list(brands_for_type), key='brand_select')

# 4. Model seçimi
if selected_brand != '...':
    models_for_brand = brands[(brands['type'] == selected_type) & (brands['brand'] == selected_brand)]['model'].unique()
    selected_model = st.sidebar.selectbox('Model', options=['...'] + list(models_for_brand), key='model_select')
else:
    selected_model = '...'

# 5. Engine seçimi
if selected_model != '...':
    engine_for_model = brands[(brands['type'] == selected_type) & (brands['brand'] == selected_brand) & (brands['model'] == selected_model)]['engine (l)'].unique()
    selected_engine = st.sidebar.selectbox('Engine (l)', options=['0.0'] + list(engine_for_model), key='engine_select')
else:
    selected_engine = '0.0'

# 6. Run (km) seçimi
run_km = st.sidebar.number_input('Run (km)', min_value=0, value=0, key='run_km_input')

# Seçimləri göstər
st.write(f'Year: {year}')
st.write(f'Type: {selected_type}')
st.write(f'Brand: {selected_brand}')
st.write(f'Model: {selected_model}')
st.write(f'Engine (l): {selected_engine}')
st.write(f'Run (km): {run_km}')

# Proqnoz üçün düymə
if st.sidebar.button('Predict', key='predict_button'):
    if selected_brand != '...' and selected_model != '...':
        # Proqnoz üçün input məlumatlarını hazırlayırıq
        input_data = pd.DataFrame({
            'year': [year],
            'engine (l)': [float(selected_engine)],
            'run (km)': [run_km],
            'brand_encoded': [encoded_brand.transform([selected_brand])[0]],
            'model_encoded': [encoded_model.transform([selected_model])[0]]
        })

        # Proqnoz edirik
        price_prediction = model.predict(input_data)

        st.write(f'Predicted price (AZN): {price_prediction[0]:.2f}')
    else:
        st.write('Brand and Model must be selected.')
