import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose
        self.RESOLUTION_BITS = 10
    def deinit(self):
        self.bus.close()
    def get_number(self):
        data = self.bus.read_word_data(self.address,0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"принятые данные: {data}, "
            f" старший бит: {upper_data_byte:x}, "
            f"младший бит: {lower_data_byte:x}, "
            f"число: {numder}")
        return number

    def get_voltage(self):
        number = self.get_number()
        voltage = number / (2 ** self.RESOLUTION_BITS) * self.dynamic_range

        if self.verbose:
            print(f"Напряжение: {voltage:.3f} B")
        return voltage
if __name__ == '__main__':
    adc = None
    try:
        adc = MCP3021(dynamic_range = 5.0)
        while True:
            voltage = adc.get_voltage()
            print(f"Напряжение на вхожу АЦП: {voltage:.3f}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n Остановалено пользователем")
    finally:
        if adc is not None:
            adc.deinit()


            