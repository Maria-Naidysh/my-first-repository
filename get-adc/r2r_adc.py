import RPi.GPIO as GPIO
import time
class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def deinit(self):
        try:
           GPIO.cleanup()
        except Exception:
            pass
    def number_to_dac(self, number):
        # подаем число на вход ЦАП
        bit_str =  bin(number)[2:].zfill(8)
        bits = [int(bit) for bit in bit_str]
        if self.verbose:
            print(f"Число на вход ЦАП {number}, биты: {bits}")
        GPIO.output(self.bits_gpio, bits)

    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                return number
        return 255
    def get_sc_voltage(self):
        #возвращает измеренное напряжение в вольтах
        number = self.sequential_counting_adc()
        voltage = number/255*self.dynamic_range
        if self.verbose:
            print(f"Код АЦП: {number}, напряжение: {voltage:.3f}")
        return voltage
    def successive_approximation_adc(self):
        result = 0
        for bit in range(7, -1, -1):
            test_value = result | (1 << bit)
            self.number_to_dac(test_value)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 0:
                result = test_value
        return result
    def get_sar_voltage(self):
        number = self.successive_approximation_adc()
        voltage = (number/255.0)*self.dynamic_range
        if self.verbose:
            print(f"SAR Код АЦП{number}, напряжение {voltage:.3f} В")
        return voltage

if __name__ == "__main__":
    adc = None
    #try: 
    #    adc = R2R_ADC(dynamic_range=3.183)
    #    while True:
    #        voltage = adc.get_sar_voltage()
    #        print(f"Измеренное напряжение SAR: {voltage:.3f}")
    
 
    try:
        adc = R2R_ADC( dynamic_range=3.183, compare_time=0.01, verbose=True)
        while True:
            voltage = adc.get_sc_voltage()
            print(f"Измеренное напряжение: {voltage:.3f}")
    finally:
        if adc is not None:
            adc.deinit()
