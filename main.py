import random as rnd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class indications:
    def __init__(self,dataframe,sensor_drift,noise,overheating,vibration,temperature):
        self.dataframe = dataframe
        self.sensor_drift = sensor_drift
        self.noise = noise
        self.overheating = overheating
        self.vibration = vibration
        self.temperature = temperature
