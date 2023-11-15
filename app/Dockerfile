FROM python:3.10 as builder

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-slim as runner

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY main.py .

# CMD ["python", "main.py"]
