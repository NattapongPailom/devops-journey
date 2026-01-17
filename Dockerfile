FROM python:3.9-slim

WORKDIR /app

COPY system_info.py .

CMD ["python", "system_info.py"]
