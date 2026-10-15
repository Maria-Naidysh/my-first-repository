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
def plot_sampling_period_hist(time):
    sampling_periods = []
    for i in range(1, len(time)):
        sampling_periods.append(time[i] - time[i-1])

    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods)
    plt.title("Гистограмма периодов измерений")
    plt.xlabel("Период измерений, с")
    plt.ylabel("Кол-во измерений")

    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()



