from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stop):
    mixer.init()
    mixer.music.load(file)
    while True:
        mixer.music.play(-1)
        inp = input()
        if inp == stop:
            mixer.music.stop()
            break
def logs(action):
    with open('logs.txt','a') as file:
        file.write(f"{action} at {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_secs = 5
    eyes_secs = 7
    exercise_secs = 9

    while True:
        if time() - init_water > water_secs:
            print("Time to have some water, enter w after drinking a glass")
            musiconloop('water.wav', 'w')
            init_water = time()
            logs("Drank water")
        if time() - init_eyes > eyes_secs:
            print("Time to give some rest to eyes, enter e after meditating for 5 mins")
            musiconloop('eyes.wav', 'e')
            init_eyes = time()
            logs("Meditated")
        if time() - init_exercise > exercise_secs:
            print("Time to do some physical activity, enter p after completing")
            musiconloop('exercise.wav', 'p')
            init_exercise = time()
            logs("Did physical activity")

