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
