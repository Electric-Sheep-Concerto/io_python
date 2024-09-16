import paho.mqtt.client as mqtt
import random
import hardware  # Import hardware functions
import time
import os  # Import os module to read environment variables
import RPi.GPIO as GPIO

def on_connect(client, userdata, flag, rc):
    # Read environment variable
    is_demo_mode = os.getenv('isDemoMode', 'false').lower() == 'true'
    user_id = os.getenv('userID')
    
    print(is_demo_mode)
    
    button_press_count = 0
    
    while True:
        if hardware.wires_connected():
            if is_demo_mode:
                # Demo mode: Only one button press required
                print("Demo mode: Waiting for button input...")
                if GPIO.input(hardware.PIN_RIGHT_BUTTON) == GPIO.LOW:  #right_botton = 12
                    button_press_count += 1  # Increment button press count
                    #print("Button pressed {} times. Processing...", button_press_count)
                    
                    # Publish user_id + button press count
                    message = "{}{}".format(user_id, button_press_count)
                    client.publish("sheep/concerto", "I'm god")
                    client.publish("sheep/concerto", message)
                    print("Published message: {}", message)

                    # Debounce delay to avoid multiple triggers for one press
                    time.sleep(0.5)
                    
            else:
                # Standard mode: Generate 4-bit pattern
                print("Wires connected. Waiting for button input...")
                bit_pattern = hardware.record_button_presses()
                print("Generated 4-bit pattern: {}", format(bit_pattern))
                client.publish("sheep/concerto", "4-bit pattern: {}".format(bit_pattern))
        else:
            print("Wires not connected.")
        time.sleep(1)  # Delay to avoid excessive CPU usage

def on_message(client, userdata, msg):
    if "LOG>" in msg.payload.decode() or str(client._client_id) == clientId:
        return
    else:
        # Play sound when message is received (placeholder function)
        play("sample.mp3")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

if __name__ == "__main__":
    clientId = random.randint(1, 1000)
    client = mqtt.Client(client_id=str(clientId))
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    try:
        client.connect("broker.hivemq.com")
        client.loop_forever()
    except KeyboardInterrupt:
        print("Program interrupted. Cleaning up GPIO.")
        hardware.cleanup_gpio()  # Clean up GPIO on exit
