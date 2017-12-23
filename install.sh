#!/usr/bin/env bash
chmod +x myip.py
mkdir ~/.myip
mv myip.py ~/.myip
ln -s ~/.myip/myip.py /usr/sbin/myip
