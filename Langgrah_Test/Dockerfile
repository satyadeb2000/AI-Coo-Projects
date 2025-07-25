# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt if it exists, otherwise install FastAPI and Uvicorn directly
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt || pip install --no-cache-dir fastapi uvicorn

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 8000 for the app
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 