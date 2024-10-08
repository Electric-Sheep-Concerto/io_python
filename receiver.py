from lib.constant import clientId
import paho.mqtt.client as mqtt
from lib.player import play
import random
from datetime import datetime
from lib.res_normal import get_normal_sample_data
import os
from lib.demo.get_path import get_demo_path

demo_users = [] # [case1 user1, case1 user2, case2 user1, case2 user2]
demo_user_index = [] # [case1 user1 index, case1 user2 index, case2 user1 index, case2 user2 index]

def on_connect(client, userdata, flag, rc):
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Connected with result code {rc}")
    client.subscribe("sheep/concerto")
    client.publish("sheep/concerto", f"LOG> {str(client._client_id.decode())}: listener connected(RX)")

def on_message(client, userdata, msg):
    message_content = msg.payload.decode().split("#")[0]
    if "LOG>" in message_content or clientId in message_content.split(":")[0]: # ログ出力
        print(message_content)
        return
    else:
        print(f"LOG> {str(client._client_id)}: {message_content}")
        #### Play music
        if os.getenv("isDemoMode") == "True" or "DBG>" in message_content:
            audio_user = message_content.split(":")[0].split(">")[1].replace(" ", "")
            audio_key = message_content.split(":")[1].replace(" ", "")
            audio_path = get_demo_path(audio_user, audio_key)
        else:
            audio_path = f"src/nor/{get_normal_sample_data(msg.payload.decode().split(':')[1].replace(' ', ''))}.mp3"
        play(audio_path)

def on_disconnect(client, userdata, rc):
    if  rc != 0:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Unexpected disconnection.")

if __name__ == "__main__":
    client = mqtt.Client(client_id=str(random.randint(1000, 9999)))
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect("broker.hivemq.com")

    client.loop_forever()