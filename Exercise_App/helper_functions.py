import numpy as np
import random


def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle

def calorie_counter(exercise):
    if exercise=="pushup":
        return float(format(random.uniform(0.3 , 0.6) , '.2f'))
    elif exercise=="squat":
        return float(format(random.uniform(0.32 , 0.4) , '.2f'))
    elif exercise=="lunges": #With 1 lunge you will burn approxiamtely 0.3 calories.
        return float(format(0.3, '.2f'))
    elif exercise=="crunches": #Doing the math, this means one Crunch equals 0.25 calories
        return float(format(0.25 , '.2f'))
    elif exercise=="jumping":#You'll burn about 100 calories doing 500 jumping jacks a day
        return float(format(5 , '.2f'))
    elif exercise=="legraise":#If you do calisthenic leg lifts for 10 minutes and you weigh 150 pounds, you'll burn about 40 calories.
        return float(format(random.uniform(0.15 , 0.3) , '.2f'))
    elif exercise=="flutterkick":#340 calories per hour   (based on a body weight of 150 lbs.)
        return float(format(random.uniform(0.05 , 0.09) , '.2f'))
    elif exercise=="hipraise":#
        return float(format(random.uniform(0.05 , 0.09) , '.2f'))
    elif exercise=="seatedinandout":#You burn 0.1875 Calories for every 10 reps with that weight
        return float(format(0.01875, '.2f'))
    elif exercise=="toetouches":# In the average 30-minute stretching session, a 155-pound person burns about 150 calories
        return float(format(random.uniform(0.083 , 0.125) , '.2f'))
    elif exercise=="high_knee":# If you're working at a moderate pace, you can expect to use about 3.5–7 calories per minute (1)
        return float(format(random.uniform(0.058 , 0.11), '.2f'))
    elif exercise=="dumbbelpress":# 125-pound individual burns between 180 and 360 calories for every hour of weight lifting
        return float(format(random.uniform(0.1 , 0.2), '.2f'))
        
        