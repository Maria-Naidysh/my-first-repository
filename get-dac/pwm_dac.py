import RPi.GPIO as GPIO
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = float(dynamic_range)
        self.verbose = verbose

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)
        
    def deinit(self):
        if getattr(self, "pwm", None) is not None:
            self.pwm.stop()
            self.pwm = None
        GPIO.cleanup(self.gpio_pin)
    def __del__(self):
        try:
            self.deinit()
        except Exception:
                pass

    def set_voltage(self, voltage):
        voltage = float(voltage)
        if voltage < 0:
            if self.verbose:
                print(f"Напряжение меньше нуля. Установлено 0 В.")
                voltage = 0.0
        elif voltage > self.dynamic_range:
            if self.verbose:
                print(
                    f"Напряжение выше диапазона."
                    f"Установлено {self.dynamic_range} B."
                )
                voltage = self.dynamic_range
        duty = voltage/self.dynamic_range*100.0
        self.pwm.ChangeDutyCycle(duty)
        if self.verbose:
            print(f"Установлено {voltage:.3f} B -> duty = {duty:.2f}%")
if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("ВЫ ввели не число, попробуйте еще раз\n")
    finally:
        dac.deinit()
            

