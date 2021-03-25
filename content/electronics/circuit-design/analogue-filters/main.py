import csv
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    create_freq_response_plot()
    create_sallen_key_response_plot()

def parse_row(data_in):
    out = np.array(data_in)
    out = out[1:-1]
    out = out.astype(float)
    return out

def get_freq_mag_phase(csv_file_path):
    with csv_file_path.open() as f:
        reader = csv.reader(f, delimiter=';')
        rows = [ row for row in reader ]
        freq_data = parse_row(rows[0])
        vout_mag_data = parse_row(rows[1])
        vout_phase_data = parse_row(rows[2])
    return {
        'freq': freq_data,
        'vout_mag': vout_mag_data,
        'vout_phase': vout_phase_data,
    }

def create_freq_response_plot():

    RESISTANCE_OHMS = 1e3
    CAPACITANCE_FARADS = 1e-6
    V_IN_VOLTS = 5.0

    LOG_X_MIN = 0
    LOG_X_MAX = 5

    freq_data = np.logspace(LOG_X_MIN, LOG_X_MAX, num=100)

    # Xc = 1 / (2pi fC)
    x_c_data = 1 / (2*np.pi*freq_data*CAPACITANCE_FARADS)

    # Vout = Vin * (Xc / ( sqrt(Xc^2 + R^2) ))
    v_out_data = V_IN_VOLTS*(x_c_data/np.sqrt(x_c_data**2 + RESISTANCE_OHMS**2))

    phase_shift_deg = np.rad2deg(-1*np.arctan(2*np.pi*freq_data*RESISTANCE_OHMS*CAPACITANCE_FARADS))

    fig, ax = plt.subplots(1)

    line1, = ax.plot(freq_data, v_out_data, label='$|V_{out}|$')
    ax2 = ax.twinx()
    line2, = ax2.plot(freq_data, phase_shift_deg, label='$\phi(V_{out})$', color='C2')

    f_cutoff = 1 / (2*np.pi*RESISTANCE_OHMS*CAPACITANCE_FARADS)
    ax.axvline(x=f_cutoff, color='C1')

    ax.set_xscale('log')
    ax.set_xlabel('Frequency f (Hz)')

    x_ticks = [ 10**x for x in range(LOG_X_MIN, LOG_X_MAX + 1) ]
    x_ticks_labels = [ str(x) for x in x_ticks ]
    x_ticks.append(f_cutoff)
    x_ticks_labels.append('$f_c$')

    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_ticks_labels)
    ax.set
    ax.set_ylabel('$V_{out}$ Magnitude V (V)')

    ax2.set_ylabel('$V_{out}$ Phase $\phi$ (deg)')
    ax2.set_ylim(-135, 45)

    ax.set_title('Frequency Response of a Low-Pass RC Filter')

    lines = [ line1, line2 ]
    ax.legend(lines, [line.get_label() for line in lines ])

    plt.tight_layout()
    plt.savefig('rc-low-pass-filter-frequency-response.png')

def create_sallen_key_response_plot():
        # Low-pass filter comparison plots

    data = get_freq_mag_phase(Path('low-pass-sallen-key/sim-results.csv'))

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 5), squeeze=False)

    ax = axes[0][0]
    color = 'C0'
    ln1 = ax.plot(data['freq'], data['vout_mag'], label='Gain', color=color)
    ax.set_title('Response Of A Low-Pass Sallen-Key Filter\n$f_c=1kHz$')
    ax.set_xlabel('Frequency f (Hz)')
    ax.set_xscale('log')
    ax.set_ylabel('Gain (dB)', color=color)
    ax.tick_params(axis='y', labelcolor=color)

    ax2 = ax.twinx()
    color = 'C1'
    ln2 = ax2.plot(data['freq'], data['vout_phase'], label='Phase', color=color)
    ax2.set_ylabel('Phase Shift ($^{\circ}$)', color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    lns = ln1 + ln2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc=0)


    ax.axvline(1e3, color='gray', linestyle='--') # Add line at fc
    

    # ax = axes[1]
    # ax.plot(data[idx]['freq'], data[idx]['vout_phase'], label=config_entry['legend'])
    # ax.set_title('Phase Response Of Different Low-Pass Filters\nfc=1kHz')
    # ax.set_xlabel('Frequency f (Hz)')
    # ax.set_xscale('log')
    # ax.set_ylabel('Gain (dB)')
    # ax.axvline(1e3, color='gray', linestyle='--') # Add line at fc
    # ax.legend()

    plt.tight_layout()
    plt.savefig('low-pass-sallen-key/response.png')


def create_low_pass_filter_comparison_plots():
    # Low-pass filter comparison plots

    data = [ get_freq_mag_phase(config_entry['data_path']) for config_entry in config ]

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))

    ax = axes[0]
    for idx, config_entry in enumerate(config):    
        ax.plot(data[idx]['freq'], data[idx]['vout_mag'], label=config_entry['legend'])
    ax.set_title('Gain Response Of Different Low-Pass Filters\nfc=1kHz')
    ax.set_xlabel('Frequency f (Hz)')
    ax.set_xscale('log')
    ax.set_ylabel('Gain (dB)')
    ax.axvline(1e3, color='gray', linestyle='--') # Add line at fc
    ax.legend()

    ax = axes[1]
    for idx, config_entry in enumerate(config):
        ax.plot(data[idx]['freq'], data[idx]['vout_phase'], label=config_entry['legend'])
    ax.set_title('Phase Response Of Different Low-Pass Filters\nfc=1kHz')
    ax.set_xlabel('Frequency f (Hz)')
    ax.set_xscale('log')
    ax.set_ylabel('Gain (dB)')
    ax.axvline(1e3, color='gray', linestyle='--') # Add line at fc
    ax.legend();

if __name__ == '__main__':
    main()