# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script into the container
COPY convert_timestamp.py .

# Command to run your script
CMD ["python", "get_timestamp.py"]