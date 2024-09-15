# Concertol

## セットアップ

```bash
> git clone https://github.com/

> nohup python tx.py &

> nohup python rx.py &

```

## RX (送出部分)

### ボタンからの入力部分

ボタンからの入力を右足を0とし左足を1として入力しています。  
入力値をもとに8bitのデータとして成型しMQTT(Message Queuing Telemetry Transport)プロトコルを活用してデータを送信しています。

## LX (受信部分)

### MQTTサーバーとの疎通
