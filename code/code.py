import time
import board
from digitalio import DigitalInOut, Pull
from adafruit_debouncer import Debouncer
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import neopixel

time.sleep(1)

switch_a_output = Keycode.Z
switch_b_output = Keycode.X

#  Keyboard
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# Key setup
switch_a_in = DigitalInOut(board.GP10)
switch_b_in = DigitalInOut(board.GP11)
switch_a_in.pull = Pull.UP
switch_b_in.pull = Pull.UP
switch_a = Debouncer(switch_a_in)
switch_b = Debouncer(switch_b_in)

# NeoPixel setup
WHITE = 0xCCCCCC
BLACK = 0x000000
ONE = 0xEC4899
TWO = 0x8B5CF6

pixel_pin = board.GP0
pixels = neopixel.NeoPixel(pixel_pin, 2, brightness=1.0)
pixels.fill(BLACK)
time.sleep(0.3)
pixels.fill(WHITE)
time.sleep(0.3)
pixels.fill(BLACK)
time.sleep(0.3)
pixels[0] = ONE
pixels[1] = TWO

last_position = encoder.position

while True:
    switch_a.update()
    switch_b.update()

    if switch_a.fell:
        keyboard.press(switch_a_output)
    if switch_a.rose:
        keyboard.release(switch_a_output)

    if switch_b.fell:
        keyboard.press(switch_b_output)
    if switch_b.rose:
        keyboard.release(switch_b_output)
