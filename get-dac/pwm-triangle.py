import pwm_dac as pwm 
import signal_generator as sg
import time

amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12,500,3.290, False)
    t = 0.0
    dt = 1.0 / sampling_frequency

    while True:
        phase = (signal_frequency*t) % 1.0
        normalized = 1 - abs(2*(phase - 0.5))
        voltage = amplitude*normalized
        dac.set_voltage(voltage)
        t += dt
        sg.wait_for_sampling_period(sampling_frequency)
        
finally:
    if 'dac' in locals():
        dac.deinit()
