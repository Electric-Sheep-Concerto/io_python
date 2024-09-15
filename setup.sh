#!/bin/bash
ble_mac="$BLE_MAC"
sudo bluetoothctl << EOF
if [ $BLE_MAC ]; then
    pair $ble_mac
    trust $ble_mac
    connect $ble_mac || true
    exit
    echo "Connected to $ble_mac"
else
    exit 1
fi
nohup python tx.py &
nohup python rx.py &
EOF