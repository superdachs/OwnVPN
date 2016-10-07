#!/bin/bash

CONF=$1
COMMAND=$2

/usr/bin/systemctl $COMMAND openvpn@$CONF

