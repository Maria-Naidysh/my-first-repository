import time 
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time

adc = R2R_ADC(dynamic_range = 3.183, compare_time=0.0001)
voltage_values = []
time_values = []

duration = 3.0
try:
    start_time = time.time()
    while(time.time() - start_time) < duration:
        current_voltage = adc.get_sc_voltage()
        voltage_values.append(current_voltage)
        current_time = time.time() - start_time
        time_values.append(current_time)
    plot_voltage_vs_time(time_values, voltage_values, max_voltage = 3.183)
finally:
    adc.deinit()