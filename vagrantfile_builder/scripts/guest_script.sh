#!/usr/bin/env bash

cat <<EOT >>  /vagrant/output.txt
#ip addr:
$(ip addr)
#ip route:
$(ip route)
EOT