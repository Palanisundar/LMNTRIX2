import cv2
import os

video='project_video.mp4'
initial_time=12000
final_time=16000
step=200

d_name ='problem/'
if not os.path.exists(d_name):
    os.makedirs(d_name)

captured=cv2.VideoCapture(video)
for i, time in enumerate(range(initial_time, final_time, step)):
    captured.set(cv2.CAP_PROP_POS_MSEC, time)
    success, img=captured.read()
    if success:
       # Need to create the directory ( 'highway') first 
       file='problem/frame{:03d}.jpg'.format(i+1)   
       cv2.imwrite(file,img)
