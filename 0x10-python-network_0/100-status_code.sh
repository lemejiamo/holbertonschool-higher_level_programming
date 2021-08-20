#!/bin/bash
# print stdout the status code of page
curl -o /dev/null -s --head -w '%{http_code}' "$1"
