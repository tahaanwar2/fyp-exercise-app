import imp
from exercises import squat, pushup, lunges, crunches, jumping, legraise, flutterkick, hipraise, seatedinandout, toetouches, highknee, dumbbelpress
import mediapipe as mp
import cv2
import streamlit as st


with open("design.css", "r") as css_file:
    st.markdown(f'<style>{css_file.read()}</style>', unsafe_allow_html=True)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

Squat = squat.Squat()
Pushup = pushup.Pushup()
Lunges = lunges.Lunges()
Crunches = crunches.Crunches()
Jumping = jumping.Jumping()
Legraise = legraise.Legraise()
Flutterkick = flutterkick.Flutterkick()
Hipraise = hipraise.Hipraise()
Seatedinandout = seatedinandout.Seatedinandout()
Toetouches = toetouches.Toetouches()
HighKnee = highknee.Highknee()
Dumbbelpress = dumbbelpress.Dumbbelpress()

st.title('Excercise')

col1, col2, col3, col4, col5, col6 = st.columns(6)
col7, col8, col9, col10, col11, col12 = st.columns(6)

Pushup.start_exercise(mp_drawing=mp_drawing, mp_pose=mp_pose,
                      col=col1, video_path=0) #'videos/pushups.mp4'
Squat.start_exercise(mp_drawing=mp_drawing, mp_pose=mp_pose,
                     col=col2, video_path=0) #'videos/squat.mp4'
Lunges.start_exercise(mp_drawing=mp_drawing, mp_pose=mp_pose,
                      col=col3, video_path=0) #'videos/lunges.mp4'
Crunches.start_exercise(mp_drawing=mp_drawing, mp_pose=mp_pose,
                        col=col4, video_path=0) #'videos/crunches.mp4'
Jumping.start_exercise(mp_drawing=mp_drawing, mp_pose=mp_pose,
                       col=col5, video_path=0) #'videos/jumping.mp4'
Legraise.start_exercise(mp_drawing=mp_drawing, mp_pose=mp_pose,
                        col=col6, video_path=0) #'videos/leg_raise.mp4'
Flutterkick.start_exercise(mp_drawing=mp_drawing, mp_pose=mp_pose,
                           col=col7, video_path=0) #'videos/flutter_kick.mp4'
Hipraise.start_exercise(mp_drawing=mp_drawing, mp_pose=mp_pose,
                        col=col8, video_path=0) #'videos/hip_raises.mp4'
Seatedinandout.start_exercise(mp_drawing=mp_drawing, mp_pose=mp_pose,
                              col=col9, video_path=0) #'videos/seated_in_and_outs.mp4'
Toetouches.start_exercise(mp_drawing=mp_drawing, mp_pose=mp_pose,
                          col=col10, video_path=0) #'videos/toe_touches.mp4'
HighKnee.start_exercise(mp_drawing=mp_drawing, mp_pose=mp_pose,
                          col=col11, video_path=0) #'videos/high_knee.mp4'
Dumbbelpress.start_exercise(mp_drawing=mp_drawing, mp_pose=mp_pose,
                          col=col12, video_path=0) #'videos/dumbbel_press.mp4'