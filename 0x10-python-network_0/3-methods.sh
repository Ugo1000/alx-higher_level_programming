#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -s -i -L -X OPTIONS "$1"
