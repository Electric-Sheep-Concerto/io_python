from lib.constant import clientId
import paho.mqtt.client as mqtt
from lib.player import play
import random

def on_connect(client, userdata, flag, rc):
    client.publish("sheep/concerto", f"LOG> {str(client._client_id.decode())}: listener connected(RX)")

def on_message(client, userdata, msg):
    if "LOG>" in msg.payload.decode() or str(client._client_id.decode()) == clientId: # ログ出力
        return
    else:
        print(f"LOG> {str(client._client_id)}: {msg.payload.decode()}")
        #### Play music
        play("sample.mp3")
        pass

def on_disconnect(client, userdata, rc):
    if  rc != 0:
        print("Unexpected disconnection.")

if __name__ == "__main__":
    client = mqtt.Client(client_id=str(random.randint(1000, 9999)))
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    client.connect("broker.hivemq.com")

    client.loop_forever()