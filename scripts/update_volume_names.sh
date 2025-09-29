#!/bin/bash -ex

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 OLD_PROJ_DIR_NAME NEW_PROJ_DIR_NAME"
    exit 1
fi

OLD_PROJ_DIR_NAME=$1
NEW_PROJ_DIR_NAME=$2

VOLUMES=("media_volume" "postgres_data" "static_volume")

for vol_name in ${VOLUMES[@]}; do
  docker volume create --name ${NEW_PROJ_DIR_NAME}_${vol_name}
  docker run --rm -it -v ${OLD_PROJ_DIR_NAME}_${vol_name}:/from -v ${NEW_PROJ_DIR_NAME}_${vol_name}:/to alpine ash -c 'cd /from ; cp -av . /to'
  docker volume rm ${OLD_PROJ_DIR_NAME}_${vol_name}
done
