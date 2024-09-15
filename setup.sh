#!/bin/bash
ble_mac="$BLE_MAC"
if [ $BLE_MAC ]; then
    sudo bluetoothctl << EOF
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