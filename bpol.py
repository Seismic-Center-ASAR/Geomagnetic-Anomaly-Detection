import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Load data
df = pd.read_csv('fdata.csv')

# Convert datetime column to datetime type
df['datetime'] = pd.to_datetime(df['Date/Time (UT)'])

# Filter data intervals, modify dates with your target interval
df_filtered = df[(df['datetime'] >= '2023-3-17') & (df['datetime'] <= '2023-3-20')]
#df_filtered = df[df['datetime'].dt.date == pd.to_datetime('2004-10-27').date()]


# Calculate BPOL
df_filtered['BPOL'] = np.sqrt(df_filtered['X (nT)']**2 + df_filtered['Y (nT)']**2 + df_filtered['Z (nT)']**2) #This line calculates the magnitude of the geomagnetic field vector using the three components X, Y, and Z, which are measured in nanotesla (nT). The magnitude is calculated using the square root of the sum of the squares of the X, Y, and Z components at each time point. This magnitude is commonly referred to as the total intensity or the magnetic field strength. The resulting values are stored in a new column named 'BPOL' in the filtered dataframe 'df_filtered'.

# Group data by datetime and resample to 1-minute means
df_resampled = df_filtered.set_index('datetime').resample('1T').mean().reset_index()

# Calculate ULF band-pass filter
fs = 1/(60)  # Sampling frequency (1 sample per minute)
fmin = 0.001
fmax = 0.0083
b, a = signal.butter(4, [fmin*2/fs, fmax*2/fs], btype='band') #Here, fmin and fmax are the lower and upper cutoff frequencies of the band, respectively. They are set to 0.001 and 0.0083 Hz, respectively, as specified in the comments in the code. The signal.butter function is used to create a Butterworth filter with a 4th order, and the resulting filter coefficients b and a are used with the signal.filtfilt function to filter the data.

# Filter data with ULF band-pass filter
df_resampled['BPOL_filtered'] = signal.filtfilt(b, a, df_resampled['BPOL'])

# Calculate statistical analysis based on standardized random variable equation
mean = df_resampled['BPOL_filtered'].mean()
std = df_resampled['BPOL_filtered'].std()
df_resampled['BPOL_standardized'] = (df_resampled['BPOL_filtered'] - mean)/std

# Plot results
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df_resampled['datetime'], df_resampled['BPOL_standardized'])
ax.axhline(y=2, color='red', linestyle='--', alpha=0.7)
ax.axhline(y=-2, color='red', linestyle='--', alpha=0.7)
ax.set_xlabel('Date')
ax.set_ylabel('Standardized BPOL')
ax.set_title('Geomagnetic Anomaly Detection')
plt.show()
#The red lines on the plot are horizontal lines at a height of 2 and -2. These lines represent the threshold values for the standardized BPOL signal. Anomalies in the geomagnetic field are detected when the standardized BPOL signal exceeds the threshold values.
#GNU Public License v.3.0 .Do not use commercially or without specifying the creator: "SEISMIC CENTER ASAR Association". Do not remove the text of the license from this code. Not to be used publicly without the permission and explicit written permission of the creator.
