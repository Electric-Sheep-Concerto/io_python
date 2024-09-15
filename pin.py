from gpiozero import LED, Button  # gpiozeroモジュールを使用
from lib.constant import URL
import time
import json
import websocket

# LEDとスイッチのGPIO番号
# デフォルトはRPZ-IR-Sensorの緑LEDと赤SW
# 必要に応じて変更
gpio_led = 17
gpio_sw = 5

# センサーの初期セットアップ
led = LED(gpio_led)
sw = Button(gpio_sw, pull_up=True)
time.sleep(0.1)

url = f"wss://{URL}/"


def on_open(ws):
    while True:
        ##
        # ここから先にセンサーの値を観測した後の処理を書く
        ##

        # スイッチが押されていた場合(ON)
        if sw.is_pressed:
            led.on()  # LED点灯
            time.sleep(5)  # 5秒待機
            led.off()  # LED消灯

        # スイッチが離されていた場合(OFF)
        else:
            led.on()  # LED点灯
            time.sleep(1)  # 1秒待機
            led.off()  # LED消灯
            print("Opened connection")
            r = {"action": "sendmessage", "message": "bot> Hello, World"}
            ws.send(json.dumps(r))


if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        url,
        on_open=on_open,
    )

    ws.run_forever()
