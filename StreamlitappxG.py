import streamlit as st
import requests
from PIL import Image
from io import BytesIO

url = 'https://github.com/OmarEltouny78/xGApp/blob/main/PL/shotmapLiverpool.png?raw=true'

url1 = 'https://raw.githubusercontent.com/OmarEltouny78/xGApp/main/xGlollipop.png'


response = requests.get(url)
img = Image.open(BytesIO(response.content))

response1 = requests.get(url1)
img1 = Image.open(BytesIO(response1.content))

st.title('xG Calculator')
st.header('What is xG in the first place?')
multi = ''' ##### Expected Goals (xG) is a metric designed to measure the probability of a shot resulting in a goal.
###### For example, a shot that have 0.2 xG means that out of every ten shots you would expect two shots to be converted to a goal.
'''
st.markdown(multi)

st.header('Why is xG important?')

multi1 = ''' ##### Expected Goals (xG) is used as a key performance indicator for a both player and team performance.
###### For example, xG can be used to calculate another important metric called Expected Points.
###### Expected points can be used to predict how many points should a team have collected from their matches (baseds on xG and xGA(Expected Goals Against)) subtract it by actual points the team have collected during the season
###### To identify, If a team is under or over performing.
'''
st.markdown(multi1)

st.header('How can xG be represented?')

st.subheader('Lollipop chart')
st.image(img1, caption='Liverpool vs Chelsea xG Lollipop')
st.markdown('###### Lollipop chart is a great way to show danger created by time over time')

st.subheader("Team's shot map")
st.image(img, caption='Liverpool shot map against Chelsea')
st.markdown('###### Shotmap chart is a great way to show where the team takes shots. The closer to the goal is a shot, the higher the xG')

st.header('Cool! I want to make something like this for "Insert favorite team name here. How?"')
multi2 = ''' ###### Well, you need to get shot data,first. You have two options. Either:
   * Web scraping shot data from websites like [Understat](http://understat.com "Understat") or [Fotmob](http://fotmob.com "Fotmob")

###### But this option does not provide xG/shot data for all leagues. For example, Understat provides shot data for only the top 5 leagues. But what fo you do when you want to create a plot for the Saudi League or the Egyptian league.
###### So there is option two:
* Collect shot data using [FC Python video event tagger](https://fcpythonvideocoder.netlify.app/ "FC Python video event tagger"). Export csv and move to the second page of this web app using the sidebar.
'''
st.markdown(multi2)

