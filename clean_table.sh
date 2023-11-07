#!/bin/bash
test -z "$1" && echo "usage: $0 raw/2023.csv" && exit 1
sed '/^[A-Z]/d' -i "$1"
