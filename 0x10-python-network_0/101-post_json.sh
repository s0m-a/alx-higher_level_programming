#!/bin/bash
#script sends JSON POST request to URL passed the first arg
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
