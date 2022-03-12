#!/bin/bash

NAME="discord_server"

docker build --no-cache --tag ${NAME} .
echo "${NAME} built with sucess"

docker run --restart unless-stopped ${NAME}