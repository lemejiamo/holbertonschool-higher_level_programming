#!/bin/bash
# post a JSON file
DESTINATION=$1
FILENAME=$2
curl -s -X POST -H "Content-Type: application/json" -d @$FILENAME $DESTINATION
