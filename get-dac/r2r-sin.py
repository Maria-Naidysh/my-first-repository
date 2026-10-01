import r2r_dac 
import signal_generator as sg
import time

amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000



try:
    dac = r2r_dac.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, False)
    t = 0.0
    dt = 1.0 / sampling_frequency

    while True:
        normalized = sg.get_sin_wave_amplitude(signal_frequency, t)
        voltage = amplitude*normalized
        dac.set_voltage(voltage)
        t += dt
        sg.wait_for_sampling_period(sampling_frequency)
        
finally:
    if 'dac' in locals():
        dac.deinit()
