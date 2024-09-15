import paho.mqtt.client as mqtt
import random
from lib.player import play

def on_connect(client, userdata, flag, rc):
    client.subscribe("sheep/concerto")
    client.publish("sheep/concerto", f"LOG> {str(client._client_id)}: listener connected")

def on_message(client, userdata, msg):
    if "LOG>" in msg.payload.decode() or str(client._client_id) == clientId: # ログ出力
        return
    else:
        #### 音声出力の処理（仮実装
        play("sample.mp3")
        pass

def on_disconnect(client, userdata, rc):
    if  rc != 0:
        print("Unexpected disconnection.")

if __name__ == "__main__":
    clientId = random.randint(1, 1000)
    client = mqtt.Client(client_id=str(clientId))
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect("broker.hivemq.com")

    client.loop_forever()