#!/bin/sh

# Log messages 
for i in {1..1000}; do
    echo "Log message $i"
    sleep 1
done

# Fail with an error message
echo "Container failed intentionally"
exit 1
