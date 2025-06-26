FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    fonts-dejavu-core \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir Pillow

COPY . .

RUN python generate_thumbs.py

EXPOSE 8000
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0"]

