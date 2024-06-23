# Use the official Python image from the Docker Hub
FROM python:3.12.3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Expose the port
EXPOSE 8501

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Command to run the application
CMD ["streamlit","run","app.py"]