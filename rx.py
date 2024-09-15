from gpiozero import LED, Button
from lib.constant import URL
import time
import paho.mqtt.client as mqtt

GPIO_SW1 = 17
GPIO_SW2 = 5

def on_connect(client, userdata, flag, rc):
    client.publish("sheep/concerto", f"{client}: sender connected", qos=1)
    ##### GPIO安定化のための待機
    time.sleep(0.1)
    while True:
        ##### GPIO処理の追加
        client.publish("sheep/concerto", f"{client}: <ここに入力コマンドを入れる>")
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