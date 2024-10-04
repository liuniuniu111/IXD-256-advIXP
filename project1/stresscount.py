import os, sys, io
import M5
from M5 import *
from hardware import *
import time

print('digital input + output toggle example')

M5.begin()

rgb2 = RGB(io=38, n=30, type="SK6812")
rgb2.set_brightness(30)
rgb2.fill_color(0x000000) 

toggle_count = 0
emergency_mode = False

input_pin = Pin(6, mode=Pin.IN, pull=Pin.PULL_UP)
input_pin_val = input_pin.value()

def set_led_color(led_index, r, g, b):
    rgb_color = (r << 16) | (g << 8) | b
    rgb2.set_color(led_index, rgb_color)


def emergency_red_flash():
    for _ in range(5):  
        for i in range(30):
            set_led_color(i, 255, 0, 0)  
        time.sleep(0.5)  
        rgb2.fill_color(0x000000)  
        time.sleep(0.5)  
    rgb2.fill_color(0x000000)  

def output_toggle():
    global toggle_count, emergency_mode

    print('Button toggled. Current count:', toggle_count)

    if toggle_count < 30:
        set_led_color(toggle_count, 0, 255, 0)  
        toggle_count += 1

        if toggle_count == 30:
            print("Emergency mode triggered!")
            emergency_mode = True
            emergency_red_flash()
            toggle_count = 0 

while True:  
    M5.update()  

    if input_pin_val == True:
        if input_pin.value() == False: 
            print('Input pin changed from high to low')
            output_toggle()

    input_pin_val = input_pin.value()  
    time.sleep_ms(100) 
