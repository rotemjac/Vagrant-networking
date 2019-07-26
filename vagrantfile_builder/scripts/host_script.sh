#!/usr/bin/env bash

FILE_PATH=$1

mkdir $FILE_PATH
cat <<EOT >>  $FILE_PATH/host.txt
#ip addr:
$(ip addr)
#ip route:
$(ip route)
EOT