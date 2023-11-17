<div align="center">

# PyDoNitor
![banner](docs/banner.png)

![main workflow](https://github.com/ashraf-minhaj/pydonitor/actions/workflows/image_manager.yml/badge.svg)&nbsp;
![test](https://github.com/ashraf-minhaj/pydonitor/actions/workflows/high_level_test.yml/badge.svg)&nbsp;
![](https://img.shields.io/badge/version-1.2%20alpha-orange?style=plastic&logo=version)&nbsp;
![](https://img.shields.io/badge/Docker--blue?style=plastic&logo=docker)&nbsp;
![](https://img.shields.io/badge/Python-3.10-blue?style=plastic&logo=python)&nbsp;
<!-- ![](https://img.shields.io/badge/Github%20Actions-white?style=plastic&logo=githubactions)&nbsp; -->
</div>

----------

Alerts on container 'state' change with crash report.

## Features
- light weight image
- get crash logs

## Future Considerations
- Discord notification system with crash logs
- Slack notification

## How to use
Nothing hard, just use `ashraftheminhaj/pydonitor` in your `docker-compose.yml`. The example below runs my_app container and checks if it is healthy, otherwise catches the log -
```yml
version: '3'

name: my_app_prod

services:
  my_app:
    container_name: my_app
    build:
      context: .
      dockerfile: Dockerfile

  pydonitor:
    tty: true
    container_name: pydonitor
    image: ashraftheminhaj/pydonitor:1.1
    environment:
      - container_name=my_app
      - discord_webhook_url=https://custom/webhook
    depends_on:
      - my_app
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

### Find me 
* linkedin [ashraf-minaj](https://www.linkedin.com/in/ashraf-minhaj)

> (c) ashraf minhaj
