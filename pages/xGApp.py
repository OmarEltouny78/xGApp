import streamlit as st

import pandas as pd

import numpy as np

import pickle

st.title('xG Model')

st.subheader('CSV file should contain x and y coordinates of the shot,isFoot (if the shoot has been taken by foot or not) and isHead (If a shot is a header or not) ')

st.markdown('**Note: there are two different models one used for regular play shots and one for non-regular play shots (shots that came from freekicks, corners, throw-ins)**')

st.markdown('***You can change the machine learning model used using the radio button below***')

st.subheader('**Here is an example dataframe**')

df=pd.read_csv('https://raw.githubusercontent.com/OmarEltouny78/xGApp/main/example.csv')

st.dataframe(df[['x','y','isFoot','isHead']],width=700)

model=None


modelOfChoice=st.radio("Choose your machine learning model",['Regular Play','Non Regular Play'])

if modelOfChoice=='Regular Play':
    model=pickle.load(open('https://github.com/OmarEltouny78/xGApp/raw/main/expected_goals_model_lr.sav', 'rb'))
else:
    model=pickle.load(open('https://github.com/OmarEltouny78/xGApp/raw/main/expected_goals_model_nonrp.sav', 'rb'))


def feature_generation(df):
    # Define pitch coordinates
    pitch_length_x = 100
    pitch_length_y = 100
    df_opta_shots_non_og_op=df.copy()
    # Create new features - 'distance_to_goal', 'distance_to_center', and 'angle'
    df_opta_shots_non_og_op['distance_to_goal'] = np.sqrt(((pitch_length_x - df_opta_shots_non_og_op['x'])**2) + ((df_opta_shots_non_og_op['y'] - (pitch_length_y/2))**2) )
    df_opta_shots_non_og_op['distance_to_center'] = abs(df_opta_shots_non_og_op['y'] - pitch_length_y/2)
    df_opta_shots_non_og_op['angle'] = np.absolute(np.degrees(np.arctan((abs((pitch_length_y/2) - df_opta_shots_non_og_op['y'])) / (pitch_length_x - df_opta_shots_non_og_op['x']))))
    return df_opta_shots_non_og_op


uploaded_file = st.file_uploader("Upload shot data file here")
if uploaded_file is not None:
    @st.cache_data
    def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    shots=pd.read_csv(uploaded_file)
    new_df=feature_generation(shots)
    final_df=shots.copy()
    final_df['xG']=model.predict_proba(new_df[['distance_to_goal','angle','isFoot','isHead']])[:,1]
    st.subheader('xG Dataframe')
    st.dataframe(final_df,width=600)
    csv = convert_df(final_df)

    st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
    )

