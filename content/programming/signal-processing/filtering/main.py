import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.signal

# Equations from https://tttapa.github.io/Pages/Mathematics/Systems-and-Control-Theory/Digital-filters/Simple%20Moving%20Average/Simple-Moving-Average.html#:~:text=The%20cutoff%20frequency%20is%20defined,)%20%E2%89%88%20%E2%88%92%203.01%20d%20B%20.

# Function for calculating the cut-off frequency of a moving average filter
def get_sma_cutoff(N, **kwargs):
    func = lambda w: np.sin(N*w/2) - N/np.sqrt(2) * np.sin(w/2)  # |H(e^jω)| = √2/2
    deriv = lambda w: np.cos(N*w/2) * N/2 - N/np.sqrt(2) * np.cos(w/2) / 2  # dfunc/dx
    omega_0 = np.pi/N  # Starting condition: halfway the first period of sin(Nω/2)
    return scipy.optimize.newton(func, omega_0, deriv, **kwargs)

N = 10 # Window size (number of samples)
fs_Hz = 1000 # Sampling frequency
f = np.linspace(0, fs_Hz/2, 1000)
w = 2*np.pi*(f/fs_Hz)
with np.errstate(divide='ignore', invalid='ignore'):
    freq_response = (1/(N**2))*((np.sin(w*N/2)**2)/(np.sin(w/2)**2))

freq_response_dB = 10*np.log10(freq_response)

# SMA coefficients
b = np.ones(N)
a = np.array([N] + [0]*(N-1))
w, h = scipy.signal.freqz(b, a, worN=4096)
f = (w*fs_Hz)/(2*np.pi) # Convert from rad/sample to Hz
freq_response_dB = 20*np.log10(abs(h))
phase_response = np.angle(h)*(180/np.pi)

w_c = get_sma_cutoff(N)
f_c_Hz = w_c * fs_Hz / (2 * np.pi)
# print(f'f_c_Hz={f_c_Hz}')

fig, axes = plt.subplots(1, 1, figsize=(10, 7), squeeze=False)
ax = axes[0][0]
ax.plot(f, freq_response_dB, label='Frequency response')
ax.axvline(fs_Hz/N, color='C1', linestyle='--', label='Window frequency')
ax.axvline(f_c_Hz, color='C2', linestyle='--', label='Cutoff frequency')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Magnitude (dB)')
ax.set_ylim(-50, 10)
ax.set_title('Magnitude Response Of SMA')
ax.legend()
plt.tight_layout()
plt.savefig('frequency-response-of-sma-magnitude.png')

fig, axes = plt.subplots(1, 1, figsize=(10, 7), squeeze=False)
ax = axes[0][0]
ax.plot(f, phase_response, label='Phase response')
ax.axvline(fs_Hz/N, color='C1', linestyle='--', label='Window frequency')
ax.axvline(f_c_Hz, color='C2', linestyle='--', label='Cutoff frequency')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Phase (°)')
ax.set_ylim(-180, 90)
ax.set_yticks([-180, -135, -90, -45, 0, 45, 90])
ax.set_title('Phase Response Of SMA')
ax.legend()
plt.tight_layout()
plt.savefig('frequency-response-of-sma-phase.png')