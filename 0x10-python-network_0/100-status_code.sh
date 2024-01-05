#!/bin/bash
#Sends GET request to the URL, and displays body of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
