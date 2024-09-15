from lib.constant import clientId
import paho.mqtt.client as mqtt
from lib.player import play

def on_connect(client, userdata, flag, rc):
    client.publish("sheep/concerto", f"LOG> {str(client._client_id)}: listener connected")

def on_message(client, userdata, msg):
    if "LOG>" in msg.payload.decode() or str(client._client_id) == clientId: # ログ出力
        return
    else:
        #### Play music
        play("sample.mp3")
        pass

def on_disconnect(client, userdata, rc):
    if  rc != 0:
        print("Unexpected disconnection.")

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    client.connect("broker.hivemq.com")

    client.loop_forever()