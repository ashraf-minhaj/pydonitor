#!/bin/sh

# Log messages 
for i in {1..2000}; do
    echo "Log message $i"
    sleep 60
done

# Fail with an error message
echo "Container failed intentionally"
exit 1
