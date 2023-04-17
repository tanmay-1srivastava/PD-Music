import h5py
from datetime import datetime
import matplotlib.pyplot as plt

f = h5py.File(r'C:\Users\sbupi\Downloads\20230316-135110_Walk (1).h5', 'r')


## use these loops to get the key names ####
for group in f.keys() :
    print (group)
    for dset in f[group]:      
        print (dset)


## use the key names obtained from above loop
# Alias 'Sesors', '3142', 'Accelerimeter, Gyroscope, Time  to get the key values ####
# Each alias here is a subgroup


accel = (list(f['Sensors']['3142']['Accelerometer']))
gyro = (list(f['Sensors']['3142']['Gyroscope']))
time = (list(f['Sensors']['3142']['Time']))
## Time is in string, you will have to convert to timestamps
time = [datetime.fromtimestamp((x)/1000000) for x in time]

print(type(accel))
print(type(gyro))
print(type(time))


print((accel))
print((gyro))
print((time))


fig, ax = plt.subplots(6,1)

ax[0,0].plot(time, accel[0])
ax[0,0].set_xlabel('Time')
ax[0,0].set_ylabel('Accel in m/s2 (x)')
ax[0,1].plot(time, accel[1])
ax[0,1].set_xlabel('Time')
ax[0,1].set_ylabel('Accel in m/s2 (y)')
ax[0,2].plot(time, accel[2])
ax[0,2].set_xlabel('Time')
ax[0,2].set_ylabel('Accel in m/s2 (z)')



ax[1,0].plot(time, gyro[1])
ax[1,0].set_xlabel('Time')
ax[1,0].set_ylabel('Angular velocity in DPS (x)')
ax[1,1].plot(time, gyro[2])
ax[1,1].set_xlabel('Time')
ax[1,1].set_ylabel('Angular velocity in DPS (y)')
ax[1,2].plot(time, gyro[3])
ax[1,2].set_xlabel('Time')
ax[1,2].set_ylabel('Angular velocity in DPS (z)')


plt.show()
