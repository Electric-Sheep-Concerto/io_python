#!/bin/bash
ble_mac="$BLE_MAC"
sudo bluetoothctl << EOF
if pair $ble_mac; then
    trust $ble_mac
    connect $ble_mac || true
else
    exit 1
fi
nohup python tx.py &
nohup python rx.py &
EOF