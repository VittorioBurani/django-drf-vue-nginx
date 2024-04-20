#!/bin/sh
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
npm run build
rm -r ../nginx/http/vue_build ../nginx/https/vue_build
mkdir -p ../nginx/http/vue_build ../nginx/https/vue_build
cp -r dist/* ../nginx/http/vue_build/
cp -r dist/* ../nginx/https/vue_build/
