#!/bin/bash
#lists all methods accepted by the server

curl -si $1 | grep "Allow:" | cut -d ' ' -f2-
