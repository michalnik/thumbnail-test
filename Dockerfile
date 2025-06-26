FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir Pillow

COPY . .

RUN python generate_thumbs.py

EXPOSE 8000
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0"]

