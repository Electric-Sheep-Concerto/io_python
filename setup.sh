#!/bin/bash
nohup python tx.py &
echo "Started tx.py"
nohup python rx.py &
echo "Started rx.py"
EOF