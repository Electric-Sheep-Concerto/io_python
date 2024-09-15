import RPi.GPIO as GPIO
import time

# GPIO pin configuration
PIN_RIGHT_BUTTON = 12  # Right button (represents 1)
PIN_LEFT_BUTTON = 13   # Left button (represents 0)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RIGHT_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Enable pull-up resistor
GPIO.setup(PIN_LEFT_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Enable pull-up resistor

# List to store the bit pattern
bit_pattern = []

# Detect button state change and record bit
def record_bit(channel):
    global bit_pattern
    if channel == PIN_RIGHT_BUTTON:
        bit_pattern.append(1)  # Record 1 for the right button
    elif channel == PIN_LEFT_BUTTON:
        bit_pattern.append(0)  # Record 0 for the left button
    print("Current bit pattern: {}".format(''.join(map(str, bit_pattern))))

# Detect button presses via interrupt
GPIO.add_event_detect(PIN_RIGHT_BUTTON, GPIO.FALLING, callback=record_bit, bouncetime=200)
GPIO.add_event_detect(PIN_LEFT_BUTTON, GPIO.FALLING, callback=record_bit, bouncetime=200)

try:
    print("Press the buttons to generate a 4-bit pattern.")
    # Wait until 4 bits are recorded
    while len(bit_pattern) < 4:
        time.sleep(0.1)  # Pause briefly to reduce CPU load

    # Display the final bit pattern
    print("Final 4-bit pattern: {}".format(''.join(map(str, bit_pattern))))

finally:
    GPIO.cleanup()  # Clean up GPIO on program exit
