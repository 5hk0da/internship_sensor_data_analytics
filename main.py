#import vital libraries
import random as rnd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#creating class as our common indications for future values
class indications:
    def __init__(self):
        self.sensor_drift = 0
#making functions for all values
    def temperature(self):
        temp = rnd.uniform(0,45)
        print(f'The temperature is:{temp}')
        if temp < 0 or temp > 45:
            print(f'The temperature is:{temp},something went wrong')

    def overheating(self):
        over = rnd.uniform(0.1,0.2)
        print(f'The overheating is:{over}')
        if over > 100:
            print(f'The overheating is:{over},the accident is possible')

    def vibration(self):
        vibr = rnd.uniform(50,100)
        print(f'The vibraion is:{vibr}')
        if vibr
    def sensor_drift(self):
        sens = rnd.uniform(0.1,0.5)
        print(f'The sensor_drift is:{sensor_drift}')
        if sensor_drift > 0.5:
            print(f'The drift is:{sensor_drift},the accident is possible')

    def noise(self):
        noise = rnd.uniform(75,80)
        print(f'The noise is:{noise}')
        if noise > 100:
            print(f'The noise is:{noise}A,the accident is possible')

