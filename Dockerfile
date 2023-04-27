FROM python:3.9-slim-buster
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY server.py .
CMD ["python3", "server.py"]
