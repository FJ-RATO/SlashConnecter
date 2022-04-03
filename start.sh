#!/bin/bash

NAME="discord_server"

while getopts c:n: flag
do
    case "${flag}" in
        c) echo "BUILDING CACHELESS..."
           docker build --no-cache --tag ${NAME} .
           break
           ;;
	n) echo "BUILDING"
           docker build --tag ${NAME} .
           break
           ;;
    esac
done

echo "STARTING ${NAME}"
docker run --restart unless-stopped ${NAME}

