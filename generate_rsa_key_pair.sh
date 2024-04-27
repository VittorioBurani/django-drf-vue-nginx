#!/bin/bash
mkdir -p keys && cd keys
if [ $# -eq 1 ] && [[ "$1" == "-n" || "$1" == "--no-pass-phrase" ]]; then
    openssl genrsa -out private.pem 4096
    openssl rsa -in private.pem -outform PEM -pubout -out public.pem
else
    openssl genrsa -des3 -out private.pem 4096
    openssl rsa -in private.pem -outform PEM -pubout -out public.pem
fi
cd ..
