import matplotlib.pyplot as plt
def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage, marker = '.', linestyle = '-')

    plt.title("График зависимости напряжения от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")

    if len(time) > 0:
        plt.xlim(time[0], time[-1])
    else:
        plt.xlim(0, 1)
    plt.ylim(0, max_voltage)
    plt.show()