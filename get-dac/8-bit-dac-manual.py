import RPi.GPIO as GPIO
dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT)
dynamic_range = 3.3
def voltage_to_number(voltage):
    if not(0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП(0,00 - {dynamic_range:.2f} B)")
        print("Устанавливаем 0,0 B")
        return 0
    return int(voltage/dynamic_range*255)
def number_to_dac(number):
    bit_str = bin(number)[2:].zfill(8)
    bits = [int(bit) for bit in bit_str]
    print(f"Число на вход ЦАП: {number}, биты: {bits}")
    GPIO.output(dac_bits, bits)
try:
    while True:
        try:
            voltage = float(input("ВВедите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("Вы ввели не число, попробуйте еще раз\n")
finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()