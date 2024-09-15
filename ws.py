import json
from constant import URL
import websocket

url = f"wss://{URL}/"


def on_message(ws, message):
    print("received: ", message)
    r = {"action": "sendmessage", "message": f"bot> {message}"}
    ws.send(json.dumps(r))


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    print("Opened connection")
    r = {"action": "sendmessage", "message": "bot> Hello, World"}
    ws.send(json.dumps(r))


if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )

    ws.run_forever()
