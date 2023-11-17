#!/bin/sh

# # Function to log messages
# log_message() {
#     timestamp=$(date +"%Y-%m-%d %T")
#     echo "$timestamp $1" >> /app/container.log
# }

# # Log a message every second for 5 minutes
# for i in {1..300}; do
#     log_message "Log message $i"
#     sleep 1
# done

# # Fail with an error message
# log_message "Container failed intentionally"
# exit 1

#!/bin/sh

# Log messages every second for 5 minutes
for i in {1..300}; do
    echo "Log message $i"
    sleep 1
done

# Fail with an error message
echo "Container failed intentionally"
exit 1
