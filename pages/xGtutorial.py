import streamlit as st

st.title('xG How to do?')

st.header('Python Video tagging')

video_file = open('video1.mkv', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

st.markdown('''The video tagging tool works as shown in the video. You can change the team name by using the edit tags button.
First, copy the video url in the text box above. After that, write down the time of each shot as you will need it in the next step.
Click anywhere on the pitch to tag the shot events''')

st.header('Preprocessing using google sheets')

video_file1 = open('video2.mkv', 'rb')
video_bytes1 = video_file1.read()

st.video(video_bytes1)

st.markdown('''When done, export the csv file and open it in google sheets. You need to add the two columns: isFoot and isHead columns. After that, change the timestamps to the one in the video.
Make sure also that all y coordinates are close to 100.As shown at the video you should subtract y coordinate out of 100 in order to get the correct values for the model''')