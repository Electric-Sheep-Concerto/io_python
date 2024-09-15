import RPi.GPIO as GPIO
import time

# GPIO pin configuration
PIN_SIGNAL = 26  # Pin for detecting wire connection
PIN_RIGHT_BUTTON = 12  # Right button (represents 1)
PIN_LEFT_BUTTON = 13   # Left button (represents 0)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_SIGNAL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Wire connection detection with pull-down
GPIO.setup(PIN_RIGHT_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Right button input
GPIO.setup(PIN_LEFT_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # Left button input

# List to store the bit pattern
bit_pattern = []

# Function to check if wires are connected
def wires_connected():
    signal = GPIO.input(PIN_SIGNAL)
    print("Signal pin state: {}", signal)  # Debug print
    return signal == GPIO.HIGH

# Function to record button inputs and generate 4-bit pattern
def record_button_presses():
    global bit_pattern
    bit_pattern = []  # Reset the bit pattern

    while len(bit_pattern) < 8:
        if GPIO.input(PIN_RIGHT_BUTTON) == GPIO.LOW:
            bit_pattern.append(1)  # Record 1 for the right button
            time.sleep(0.2)  # Debounce delay
        elif GPIO.input(PIN_LEFT_BUTTON) == GPIO.LOW:
            bit_pattern.append(0)  # Record 0 for the left button
            time.sleep(0.2)  # Debounce delay
    
    return ''.join(map(str, bit_pattern))  # Return 4-bit as string

def cleanup_gpio():
    GPIO.cleanup()  # Clean up GPIO when finished
