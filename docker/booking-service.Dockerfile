# Build backend docker file
FROM python:3.9-slim

# set working directory
WORKDIR /app

# Copy file requirements.txt vào container
COPY booking-service/requirements.txt /app/

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn của booking-service vào container
COPY booking-service /app/booking-service

# set port
EXPOSE 5001

# set environment variables for Flask
ENV FLASK_APP=/app/booking-service/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

# run the application
CMD ["flask", "run"]