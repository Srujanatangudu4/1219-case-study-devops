# Use official lightweight Python image
FROM python:3.9-slim-buster

# Set working directory inside container
WORKDIR /app

# Copy all files into container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask default port
EXPOSE 5000

# Command to run the Flask app
CMD ["python3", "app.py"]
