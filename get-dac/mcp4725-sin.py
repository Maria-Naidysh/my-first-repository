import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000



try:
    dac = mcp.MCP4725(3.3, 0x61, False)
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
