import netCDF4
import numpy as np
import pandas as pd
from netCDF4 import Dataset

# Reading the Netcdf File

data = Dataset(r'C:\Users\Roopesh\Downloads\global_monthly_010deg.nc','r')

# Displaying the name of the variables

print(data.variables.keys())

#Accessing the variables

lon = data.variables['lon']
print(lon)

lat = data.variables['lat']
print(lat)

time = data.variables['time']
print(time)

rf = data.variables['precipitation']
print(rf)

#Accessing the data from the variables

lon_data = data.variables['lon'][:]
print(lon_data)

lat_data = data.variables['lat'][:]
print(lat_data)

time_data = data.variables['time'][:]
print(time_data)

precipitation_data = data.variables['precipitation'][:]
print(precipitation_data)



