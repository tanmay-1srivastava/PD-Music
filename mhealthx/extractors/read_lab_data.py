import h5py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig, a = plt.subplots(2,1)

f = h5py.File('/Users/tanmay-s/Downloads/20230316-135110_Walk.h5', 'r')
data = list(f['Sensors']['3142']['Accelerometer'])
a[0].plot(data)
a[0].set_title('RRAMP data')



input_file = '/Users/tanmay-s/Downloads/With Paper_2023-03-16T12.32.47.025_C52D26FB9648_Accelerometer.csv'
df = pd.read_csv(input_file)
ax = list(df['x-axis (g)'])
ax -= np.mean(ax)
ay = list(df['y-axis (g)'])
ay -= np.mean(ay)
az = list(df['z-axis (g)'])
az -= np.mean(az)


ax = [x*10 for x in ax]
ay = [x*10 for x in ay]
az = [x*10 for x in az]

a[1].plot(ax)
a[1].plot(ay)
a[1].plot(az)

a[1].set_title('MMR Data')

plt.show()