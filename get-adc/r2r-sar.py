import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

adc = R2R_ADC(dynamic_range=3.183, compare_time = 0.0001)
voltage_values = []
time_values = []

duration = 3.0

try:
    start_time = time.time()
    while (time.time() - start_time) < duration:
        voltage = adc.get_sar_voltage()
        voltage_values.append(voltage)
        current_time = time.time() - start_time
        time_values.append(current_time)
    plot_voltage_vs_time(time_values, voltage_values, max_voltage=adc.dynamic_range)
    plot_sampling_period_hist(time_values)
finally:
    adc.deinit()