'''Assume that a programmer works at the office from 9-5 pm. We have to take care of his health and remind him three things:

-To drink a total of 3.5-liter water after some time interval between 9-5 pm.
-To do eye exercise after every 30 minutes.
-To perform physical activity after every 45 minutes.
*Instructions:-
The task is to create a program that plays mp3 audio until the programmer enters the input which implies that he has done the task.

-For Water, the user should enter “Drank”
-For Eye Exercise, the user should enter “EyDone”
-For Physical Exercise, the user should enter “ExDone”
After the user entered the input, a file should be created for every task separately, which contains the details about the time when the user performed a certain task
'''



#
#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time
print("WELCOME USER:)")

def musicplay(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_time = 20*60
    exercise_time = 40*60
    eyes_time= 25*60

    while True:
        if time() - init_water > water_time:
            print("Water Drinking time!!! Enter 'drank' to stop the alarm.")
            musicplay('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyes_time:
            print("Eye exercise time!!! Enter 'doneeyes' to stop the alarm.")
            musicplay('eyes.mp3', 'done')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exercise_time:
            print("Physical Activity Time!!! Enter 'donephy' to stop the alarm.")
            musicplay('physical.mp3', 'done2')
            init_exercise = time()
            log_now("Physical Activity done at")
