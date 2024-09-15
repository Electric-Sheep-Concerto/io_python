import paho.mqtt.client as mqtt
import random
from lib.player import play

def on_connect(client, userdata, flag, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("sheep/concerto")
    client.publish("sheep/concerto", f"{client}: listener connected", qos=1)

def on_message(client, userdata, msg):
    if msg.qos == 1: # ログ出力
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