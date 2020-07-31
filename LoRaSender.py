from config import *
from machine import Pin, SPI
from sx127x import SX127x
from time import sleep

device_spi = SPI(baudrate = 10000000, 
        polarity = 0, phase = 0, bits = 8, firstbit = SPI.MSB,
        sck = Pin(device_config['sck'], Pin.OUT, Pin.PULL_DOWN),
        mosi = Pin(device_config['mosi'], Pin.OUT, Pin.PULL_UP),
        miso = Pin(device_config['miso'], Pin.IN, Pin.PULL_UP))

lora = SX127x(device_spi, pins=device_config, parameters=lora_parameters)

def send(lora):
    counter = 0
    print("LoRa Sender")

    while True:
        payload = 'Hello ({0})'.format(counter)
        print("Sending packet: \n{}\n".format(payload))
        #display.show_text_wrap("{0} RSSI: {1}".format(payload, lora.packet_rssi()))
        lora.println(payload)

        counter += 1
        sleep(5)
