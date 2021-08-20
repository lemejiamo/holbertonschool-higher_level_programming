#!/bin/bash
# Display the size of the body of the response

REQUEST_TO=$1
curl -sI "$REQUEST_TO" | awk '/Content-Length/ {print $2}'
