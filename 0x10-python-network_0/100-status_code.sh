#!/bin/bash
# print stdout the status code of page
curl -o /dev/null -s $1 -w '%{http_code}'