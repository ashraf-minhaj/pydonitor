""" ******** PyDoNitor ********

    author: ashraf minhaj
    mail: ashraf_minhaj@yahoo.com
    
    date: 16-11-2023
    Docker container monitor and alert system 
"""

import os
import time
import docker
import requests

CONTAINER_NAME          = os.getenv("container_name", "test_img")
DISCORD_WEBHOOK_URL     = os.getenv("discord_webhook_url", None)
HEALTH_CHECK_INTERVAL   = int(os.getenv("health_check_interval", "10"))

def send_notification(container_name, logs, webhook_url):
    payload = {
        'container_name': container_name,
        'details': logs
    }
    # requests.post(webhook_url, json=payload)
    print(payload)

def monitor_container(container_name, webhook_url):
    # a flag that changes when a container is running
    container_started = False
    client = docker.from_env()

    try:
        container = client.containers.get(container_name)

        while True:
            # Check container health
            container.reload()
            if container.attrs['State']['Status'] == 'running':
                # print("container is running")
                if not container_started:
                    send_notification(container_name, f"Container {container_name} running.", webhook_url)
                    container_started = True
            else:
                # If the container is not running, get and send logs
                logs = container.logs().decode('utf-8')
                send_notification(container_name, f"Container stopped, logs: {logs}", webhook_url)
                break

            time.sleep(HEALTH_CHECK_INTERVAL)

    except docker.errors.NotFound:
        print(f"Container '{container_name}' not found.")
        send_notification(container_name, f"Container '{container_name}' not found.", webhook_url)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        send_notification(container_name, f"An error occurred: {str(e)}", webhook_url)

if __name__ == "__main__":
    monitor_container(CONTAINER_NAME, DISCORD_WEBHOOK_URL)
