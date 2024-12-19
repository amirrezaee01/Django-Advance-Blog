FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy dependencies file
COPY requirements.txt /app/

# Install pip and dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy project files
COPY ./core /app/




