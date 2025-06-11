# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the default FastAPI port
EXPOSE 8000

# Start the server
CMD ["uvicorn", "source.app:app", "--host", "0.0.0.0", "--port", "8000"]