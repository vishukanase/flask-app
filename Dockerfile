# Use official Python runtime as a parent image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app source code
COPY . .

# Expose the port your Flask app runs on
EXPOSE 5000

# Set environment variable for Flask app entrypoint
ENV FLASK_APP=index.py

# Command to run the Flask app
CMD ["python", "index.py"]
