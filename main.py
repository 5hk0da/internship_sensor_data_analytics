#import vital libraries
import random as rnd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#creating class for our functions
class Indications:

    def __init__(self):

        #Normal values
        self.temp_base = 25
        self.vibration_base = 50
        self.drift_base = 0.1
        self.overheating_base = 0

        #Wear
        self.temp_wear = 0
        self.vibration_wear = 0
        self.drift_wear = 0
        self.overheating_wear = 0

    # creating temperature function with adding wear
    def temperature(self):
        self.temp_wear += rnd.uniform(0.1, 0.5)
        value = self.temp_base + self.temp_wear + rnd.uniform(-1, 1)
        print(f"Temperature: {value:.2f}°C")
        if value > 45:
            print("WARNING: OVERHEATING")

    # creating vibration function with adding wear
    def vibration(self):
        self.vibration_wear += rnd.uniform(0.2, 1)
        value = self.vibration_base + self.vibration_wear + rnd.uniform(-2, 2)
        print(f"Vibration: {value:.2f}")
        if value > 100:
            print("WARNING: CRITICAL VIBRATION")

    # creating sensor drift function with adding wear
    def sensor_drift(self):
        self.drift_wear += rnd.uniform(0.01, 0.05)
        value = self.drift_base + self.drift_wear
        print(f"Sensor drift: {value:.3f}")
        if value > 0.5:
            print("WARNING: SENSOR DEGRADATION")

    # creating overheating function with adding wear
    def overheating(self):
        self.overheating_wear += rnd.uniform(0.01, 0.03)
        value = self.overheating_base + self.overheating_wear
        print(f"Overheating: {value:.3f}")
        if value > 0.2:
            print("WARNING: OVERHEATING RISK")


robot = Indications()

for i in range(15):

    print(f"\n--- CYCLE {i+1} ---")

    robot.temperature()
    robot.vibration()
    robot.sensor_drift()
    robot.overheating()