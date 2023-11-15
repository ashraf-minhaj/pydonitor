""" ******** PyDoNitor ********

    author: ashraf minhaj
    mail: ashraf_minhaj@yahoo.com
    
    date: 15-11-2023
    Docker container monitor and alert system 
"""
import docker
import requests
import time

def send_notification(container_name, logs, webhook_url):
    payload = {
        'container_name': container_name,
        'logs': logs
    }
    # requests.post(webhook_url, json=payload)
    print(payload)

def monitor_container(container_name, webhook_url):
    # run docker daemon first
    client = docker.from_env()

    try:
        container = client.containers.get(container_name)

        while True:
            # Check container health
            container.reload()
            if container.attrs['State']['Status'] != 'running':
                # If the container is not running, get and send logs
                logs = container.logs().decode('utf-8')
                send_notification(container_name, logs, webhook_url)
                break

            # Adjust the sleep interval based on your monitoring requirements
            time.sleep(10)

    except docker.errors.NotFound:
        print(f"Container '{container_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Replace 'your_container_name' and 'your_webhook_url' with your actual container name and webhook URL
    container_name = 'your_container_name'
    webhook_url = 'your_webhook_url'

    monitor_container(container_name, webhook_url)
