# Arrhythmia Detection and other analysis 💟🩺
<img src="https://media.discordapp.net/attachments/1223174231936995390/1286010161596596317/image.png?ex=66ec59cb&is=66eb084b&hm=881addfe899e7f03e8c072eb984ba3a31f2b499480adb7c6511b5c539b2832c7&=&format=webp&quality=lossless&width=1247&height=408">
<p align="center">📈10 sec ECG REPORT📈</p>
<img src="https://media.discordapp.net/attachments/1223174231936995390/1286009422597853204/Figure_1.png?ex=66ec591b&is=66eb079b&hm=d3409a0e0372697e3a6c64859bde292441490363990a49ff5f1b8a879839a43c&=&format=webp&quality=lossless&width=1216&height=603">
<p align="center">📉OUTPUT AFTER ANALYSIS📉</p>

## ❣Overview❣
This project processes ECG data (10 sec)📈 to detect heartbeats, calculate heart rate, and assess potential arrhythmia. The code uses wavelet transforms to analyze high-frequency components of the ECG signal, such as R-peaks, and provides insights into heart rate and rhythm analysis.

## ❣Key Concepts❣:
1. 🧹**Data Loading and Cleaning**:
   - Load ECG data from a CSV file.
   - Clean the data and prepare it for further analysis.

2. 👩‍💻**Wavelet Transform (MODWT)**:
   - Perform a 4-level undecimated wavelet transform using the `sym4` wavelet.
   - Focus on **high-frequency components** to capture sharp R-peaks.
   - Filter out lower-frequency components, which represent baseline wander.

3. 🗻**R-Peak Detection**:
   - Square the magnitude of the wavelet-reconstructed signal to emphasize the R-peaks.
   - Use `scipy.signal.find_peaks` to detect R-peaks and analyze heartbeats.

4. 🩺**RR Intervals and Heart Rate Calculation**:
   - Calculate RR intervals (time between consecutive R-peaks) to measure heart rate variability.
   - Compute the heart rate in beats per minute (BPM).

5. 🩺**Arrhythmia Detection**:
   - Calculate the coefficient of variation (CV) of RR intervals to assess arrhythmia.
   - Compare CV to a predefined threshold to flag potential arrhythmic conditions.

6. 📊**Visualization**:
   - Plot the original ECG signal.
   - Mark detected R-peaks on the graph for visualization.

## Dependencies in python🐍:
- `numpy`
- `pandas`
- `matplotlib`
- `scipy`
- `pywt`



