import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import pywt
import pandas as pd

# Load the ECG data from the CSV file
file_path = 'arr_10s.csv'  # Replace with your actual file path
try:
    ecg_data = pd.read_csv(file_path)
    print("File loaded successfully!")
except Exception as e:
    print(f"Error loading file: {e}")

# Check the data
print(f"First few rows of data:\n{ecg_data.head()}")

# Skip the first row (which contains units) and clean column names
try:
    ecg_data_cleaned = ecg_data[1:]  # Skipping the first row&column
    ecg_data_cleaned.columns = ['Elapsed time','ECG I filtered','Ecg 2']  # Renaming columns properly #adjust the column according to your need
    # print("Data cleaned and columns renamed.")
except Exception as e:
    print(f"Error processing data: {e}")

# Convert the 'ECG I filtered' column to float for analysis
try:
    ecgsig_filtered = ecg_data_cleaned['ECG I filtered'].astype(float).values
    print(f"ECG signal length: {len(ecgsig_filtered)}")
except Exception as e:
    print(f"Error converting ECG signal: {e}")

# Get sampling rate from the user
Fs = float(input('Enter Sampling Rate: '))

t = np.arange(len(ecgsig_filtered))  # No. of samples
tx = t / Fs  # Time vector

# Perform 4-level undecimated wavelet transform (MODWT) using sym4
try:
    coeffs = pywt.wavedec(ecgsig_filtered, 'sym4', level=4)
    print("Wavelet decomposition successful.")
except Exception as e:
    print(f"Error in wavelet decomposition: {e}")

# Recreate an empty list for reconstruction, initializing only d3 and d4 to zero arrays
try:
    wtrec = [np.zeros_like(c) if i < 2 else c for i, c in enumerate(coeffs)]
    y = pywt.waverec(wtrec, 'sym4')  # Perform inverse DWT on the reconstructed signal using d3 and d4 coefficients
    print("Inverse DWT successful.")
except Exception as e:
    print(f"Error in inverse DWT: {e}")

# Magnitude square of the signal
y = np.abs(y) ** 2
avg = np.mean(y)  # Threshold


import numpy as np
from scipy.signal import find_peaks

try:
    # Find the peaks
    peaks, properties = find_peaks(y, height=8 * avg, distance=50)
    
    # Calculate distances between consecutive peaks (RR intervals)
    rr_intervals = np.diff(peaks)
    print("RR intervals (distances between peaks):", rr_intervals)
    
    # Calculate the mean and standard deviation of RR intervals
    mean_rr = np.mean(rr_intervals)
    std_rr = np.std(rr_intervals)
    
    # Calculate the coefficient of variation (CV) of RR intervals
    cv_rr = (std_rr / mean_rr) * 100
    print(f"Coefficient of Variation (CV) of RR intervals: {cv_rr:.2f}%")
    
    # Define a threshold for arrhythmia based on CV (this threshold is an example and may vary)
    arrhythmia_threshold = 9  # Example threshold, typically between 10-20%
    
    # Compare CV to the threshold
    if cv_rr > arrhythmia_threshold:
        print("The patient is arrhythmic.")
    else:
        print("The patient's heart rhythm is normal.")
    
    # Get peak heights and convert peak locations to integer indices
    Rpeaks = properties['peak_heights']
    locs = peaks.astype(int)
    nohb = len(locs)  # Number of heartbeats
    
    # Calculate the time limit and heartbeats per minute (BPM)
    timelimit = len(ecgsig_filtered) / Fs  # Fs is the sampling frequency
    hbpermin = (nohb * 60) / timelimit  # Beats per minute (BPM)
    #heartbeat by me
    heart_beat=nohb*6
    
    print(f'Heart Rate = {heart_beat:.2f} BPM')
    print(f"Number of heartbeats detected: {nohb}")
    
except Exception as e:
    print(f"Error finding peaks: {e}")


# Displaying ECG signal and detected R-peaks
plt.figure(figsize=(12, 8))

# Plot ECG Signal
plt.subplot(2, 1, 1)
plt.plot(tx, ecgsig_filtered)
plt.xlim([0, timelimit])
plt.grid(True)
plt.xlabel('Seconds')
plt.title('Filtered ECG Signal')

# Plot detected R-peaks
plt.subplot(2, 1, 2)
plt.plot(t, y)
plt.grid(True)
plt.xlim([0, len(ecgsig_filtered)])
try:
    plt.plot(locs, y[locs], 'ro')  # Marking R-peaks
except Exception as e:
    print(f"Error plotting R-peaks: {e}")
    
plt.xlabel('Samples')
plt.title(f'R Peaks found and Heart Rate: {heart_beat:.2f} BPM')

plt.tight_layout()
plt.show()
# standarddeviation=[]

# for x in range(1,len(ecg_data_cleaned)):
#     standarddeviation.append(abs(ecgsig_filtered[x]-avg))
# print(standarddeviation[len(standarddeviation)-1])
