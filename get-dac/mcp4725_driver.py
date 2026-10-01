import smbus

class MCP4725:
    def __init__(self, dynamic_range, address = 0x61, verbose = True):
        self.bus = smbus.SMBus(1)
        self.address = address #7 битный адрес микросхемы
        self.wm = 0x00
        self.pds = 0x00
        self.verbose = verbose
        self.dynamic_range = dynamic_range #опорное напряж

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return
        if not (0<= number <= 4095):
            print("Число выходит за разрядность (12 бит)")
            return 
        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}. 0x{second_byte:02X}]\n")
    def set_voltage(self, voltage):
        if not (0 <= voltage <= self.dynamic_range):
            print(f"Напряжение должно быть в диапазоне 0...{self.dynamic_range} В")
            return
        number = int(round(voltage/self.dynamic_range * 4095))
        self.set_number(number)

if __name__ == "__main__":
    print("программа запущена")
    dac = MCP4725(dynamic_range = 3.3, address = 0x61, verbose = True)
    try:
        voltage = float(input("Введите напряжение в вольтах: "))
        dac.set_voltage(voltage)
    finally:
        dac.deinit() 
