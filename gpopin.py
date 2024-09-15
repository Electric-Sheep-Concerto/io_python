## NOT USE

import serial
import serial.tools.list_ports
from constant import BOUD

def get_port():
    ports = []
    for port in serial.tools.list_ports.comports():
        ports.append(port.device)
    return port.device

def get_serial(port):
    serial_port=serial.Serial(port=port, baudrate=9600, parity= 'N')
    return serial_port

def gpopin_tx(content) -> None:
    #送信(tx)
    data=content+'\r\n'
    data=data.encode('utf-8')
    serial_port = get_serial(get_port())
    serial_port.write(content)
    return

def gpopin_rx() -> None:
    #受信(rx)
    data = get_serial(get_port()).readline()
    data=data.strip()
    data=data.decode('utf-8')
    return data

def serial_open():
    global Serial_Port
    
    #portリストを取得
    serial_ports={}
    for i,port in enumerate(serial.tools.list_ports.comports()):
        serial_ports[str(i)]=port.device
    
    #RaspberryPiのminiUART検出できないので、/dev/ttyAMA0があれば自動的に/dev/ttyS0を追加
    if '/dev/ttyAMA0' in serial_ports.values():
        serial_ports[str(len(serial_ports))]='/dev/ttyS0'

    port_val = serial_ports[ input(f'ポート番号を選んでください。{serial_ports}:') ]
    boud_val = int(input('ボーレートbpsを数値で入力してください。:'))
    prty_val = input(f'パリティーを選んでください。[N:None, O:Odd, E:Even]:')
    
    Serial_Port=serial.Serial(port=port_val, baudrate=BOUD)
    print(f'open{port_val}/{boud_val}bps/parity:{prty_val}')