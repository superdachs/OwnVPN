#!/bin/bash

CONF=$1
COMMAND=$2

systemctl $COMMAND openvpn@$CONF

