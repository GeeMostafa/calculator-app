# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install flask

# Expose the application port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]

