###################################
# author: chatgpt
# co-author: ashraf minhaj
# email: ashraf_minhaj@yahoo.com
# 
# date: 18-11-23
# run a shell script that will fail after some time
###################################

# Use a base image
FROM alpine:latest

# Create a directory for logs
WORKDIR /app

# Add a simple script that writes logs
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Run the script on container start
CMD ["/app/entrypoint.sh"]
