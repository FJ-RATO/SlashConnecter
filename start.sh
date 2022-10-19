#!/bin/bash

NAME="discord_server"

docker build --tag ${NAME} .
echo "STARTING ${NAME}"
docker run --restart unless-stopped ${NAME}

