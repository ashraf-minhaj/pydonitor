#########################################
# author: ashraf minhaj
# email : ashraf_minhaj@yahoo.com
# 
# date: 18-11-23
# pydonitor application, monitors docker 
# container and send notification with
# crash logs.
#########################################

FROM --platform=linux/amd64 python:3.10 as builder

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# runner stage
FROM --platform=linux/amd64 python:3.10-slim as runner

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

ENV container_name=test_img
ENV discord_webhook_url=https://custom/webhook

COPY main.py .

CMD ["python", "main.py"]
