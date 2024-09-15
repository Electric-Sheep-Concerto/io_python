from lib.constant import clientId
import paho.mqtt.client as mqtt
from lib.player import play
import random
from datetime import datetime
from lib.res_demo import get_demo_sample_data

demo_users = [] # [case1 user1, case1 user2, case2 user1, case2 user2]
demo_user_index = [] # [case1 user1 index, case1 user2 index, case2 user1 index, case2 user2 index]

def on_connect(client, userdata, flag, rc):
    print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Connected with result code {rc}")
    client.subscribe("sheep/concerto")
    client.publish("sheep/concerto", f"LOG> {str(client._client_id.decode())}: listener connected(RX)")

def on_message(client, userdata, msg):
    if "LOG>" in msg.payload.decode() or clientId in msg.payload.decode().split(":")[0]: # ログ出力
        print(msg.payload.decode())
        return
    else:
        print(f"LOG> {str(client._client_id)}: {msg.payload.decode()}")
        #### Play music
        audio_path = get_demo_sample_data(msg.payload.decode().split(":")[1].replace(" ", ""))
        play(audio_path)
        pass

def on_disconnect(client, userdata, rc):
    if  rc != 0:
        print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Unexpected disconnection.")

if __name__ == "__main__":
    client = mqtt.Client(client_id=str(random.randint(1000, 9999)))
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect("broker.hivemq.com")

    client.loop_forever()