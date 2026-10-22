from mcp3021_driver import MCP3021
from adc_plot import plot_sampling_period_hist
import matplotlib.pyplot as plt
import time

adc = MCP3021(dynamic_range = 5.0)
voltage_values = []
time_values = []
duration = 5.0
try:
    start_time = time.time()
    while(time.time() - start_time) < duration:
        voltage = adc.get_voltage()
        voltage_values.append(voltage)

        current_time = time.time() - start_time
        time_values.append(current_time)
        
    plt.figure(figsize = (10, 6))
    plt.plot(time_values, voltage_values)
    plt.title("Зависимость напряжения от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.xlim(0, duration)
    plt.ylim(0, adc.dynamic_range)
    plt.grid(True)
    plt.show()
    plot_sampling_period_hist(time_values)
finally:
    adc.deinit()