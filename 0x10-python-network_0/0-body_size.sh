#!/bin/bash
# Script to see body length
curl -s -o /dev/null -w "%{size_download}\n" http://"$1"
