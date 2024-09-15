import paho.mqtt.client as mqtt
import random
from lib.player import play
import time

def on_connect(client, userdata, flag, rc):
    client.subscribe("sheep/concerto")
    client.publish("sheep/concerto", f"LOG> {str(client._client_id.decode())}: sender connected(TX)")
    ##### Waiting
    time.sleep(0.1)
    while True:
        ##### Processing
        client.publish("sheep/concerto", f"{client}: <ここに入力コマンドを入れる>")
        time.sleep(10)
        pass

def on_message(client, userdata, msg):
    if "LOG>" in msg.payload.decode() or str(client._client_id) == clientId: # ログ出力
        return
    else:
        #### Processing
        pass

def on_disconnect(client, userdata, rc):
    if  rc != 0:
        print("Unexpected disconnection.")

if __name__ == "__main__":
    clientId = random.randint(1, 1000)
    client = mqtt.Client(client_id=str(random.randint(1000, 9999)))
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect("broker.hivemq.com")

    client.loop_forever()