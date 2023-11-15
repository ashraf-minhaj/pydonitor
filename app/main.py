""" ******** PyDoNitor ********

    author: ashraf minhaj
    mail: ashraf_minhaj@yahoo.com
    
    date: 16-11-2023
    Docker container monitor and alert system 
"""

import sys
import time
import docker
import requests

# Default values for arguments
DEFAULT_VALUES = {
    "container_name": "default_container",
    "discord_webhook_url": "None",
    "health_check_interval": 10,
}

args = dict(arg.split('=') for arg in sys.argv[1:]) if len(sys.argv) > 1 else {}    # Parse command-line arguments into a dictionary
arguments = {**DEFAULT_VALUES, **args}                                              # Merge with default values

# Access individual arguments
CONTAINER_NAME          = arguments.get("container_name")
DISCORD_WEBHOOK_URL     = arguments.get("discord_webhook_url")
HEALTH_CHECK_INTERVAL   = int(arguments.get("health_check_interval"))

def send_notification(container_name, logs, webhook_url):
    payload = {
        'container_name': container_name,
        'logs': logs
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

# python3.10 main.py container_name=blissful_carver discord_webhook_url=https://custom/webhook
