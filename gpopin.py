import serial
import serial.tools.list_ports

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
