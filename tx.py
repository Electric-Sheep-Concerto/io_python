import paho.mqtt.client as mqtt
import random
import hardware  # Import hardware functions

def on_connect(client, userdata, flag, rc):
    #client.publish("sheep/concerto", "LOG> {}: listener connected".format(str(client._client_id)))

    
    # Keep checking if wires are connected
    while True:
        if hardware.wires_connected():
            print("Wires connected. Waiting for button input...")
            # Capture 4-bit pattern from button inputs
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
