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
        print(f"Temperature: {value:.1f}°C")
        if value > 45:
            print("WARNING: OVERHEATING")

    # creating vibration function with adding wear
    def vibration(self):
        self.vibration_wear += rnd.uniform(0.2, 1)
        value = self.vibration_base + self.vibration_wear + rnd.uniform(-2, 2)
        print(f"Vibration: {value:.1f}")
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


#Creating a graph

#creating a table by using datafprame and pandas
df = pd.DataFrame(robot.data)
#size of our future grap
fig, ax = plt.subplots(figsize = (10,9))

#setting our graph
ax.plot(df["time"], df["temp"], label="Temperature")
ax.plot(df["time"], df["vibration"], label="Vibration")
ax.plot(df["time"], df["drift"], label="Drift")

#deleting right and top sides
for spine in ['top', 'right',]:
    ax.spines[spine].set_visible(False)

ax.set_title ('Robot analis data',lock = 'left',fontsize = 14,color = 'black',fontweight = 'bold',pad=15)
ax.set_xlabel('X',fontsize = 10,color = 'black')
ax.set_ylabel('Y',fontsize = 10,color = 'black')

#grid
ax.yaxis.grid(True,linestyle='--',color='grey',alpha=0.5,zorder=0)

#illustrating our graph
plt.show()
