FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src/
COPY test/ /app/test/

RUN mkdir -p /app/data
CMD ["python", "src/main.py"]
