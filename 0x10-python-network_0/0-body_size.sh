#!/usr/bin/env bash
# Display the size of the body of the response

REQUESTTO=$1
curl Content-Length $REQUESTTO
