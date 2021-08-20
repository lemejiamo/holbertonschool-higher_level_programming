#!/bin/bash
#
DESTINATION=$1
FILENAME=$2
curl -X POST -H "Content-Type: application/json" -d @$FILENAME $DESTINATION
