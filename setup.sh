#!/bin/bash
ble_mac="$BLE_MAC"
if [ $BLE_MAC ]; then
    sudo bluetoothctl <<
    pair $ble_mac
    trust $ble_mac
    connect $ble_mac || true
    exit
EOF
    echo "Connected to $ble_mac"
else
    echo "Please provide BLE_MAC"
    exit 1
fi
nohup python tx.py &
echo "Started tx.py"
nohup python rx.py &
echo "Started rx.py"
EOF