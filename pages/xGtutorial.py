import streamlit as st
import requests
from PIL import Image
from io import BytesIO
st.title('xG How to do?')

st.header('Python Video tagging')
url = 'https://raw.githubusercontent.com/OmarEltouny78/xGApp/main/Screenshot%202024-02-03%20144900.png'


url1 = 'https://raw.githubusercontent.com/OmarEltouny78/xGApp/main/Videotaggingevent.png'


response = requests.get(url)
img = Image.open(BytesIO(response.content))

response1 = requests.get(url1)
img1 = Image.open(BytesIO(response1.content))

st.subheader('Video event tagging')
st.image(img1, caption='Video event tagging')




st.markdown('''The video tagging tool works as shown in the video. You can change the team name by using the edit tags button.
First, copy the video url in the text box above. After that, write down the time of each shot as you will need it in the next step.
Click anywhere on the pitch to tag the shot events''')

st.header('Preprocessing using google sheets')

st.subheader("Google Sheet editing")
st.image(img, caption='Sheet editing')

st.markdown('''When done, export the csv file and open it in google sheets. You need to add the two columns: isFoot and isHead columns. After that, change the timestamps to the one in the video.
Make sure also that all y coordinates are close to 100.As shown at the video you should subtract y coordinate out of 100 in order to get the correct values for the model''')