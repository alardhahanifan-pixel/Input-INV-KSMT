# Dockerfile untuk Aplikasi Input Penjualan
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create instance directory for database
RUN mkdir -p instance

# Expose port
EXPOSE 8080

# Set environment variables
ENV FLASK_ENV=production
ENV HOST=0.0.0.0
ENV PORT=8080

# Command to run the application
CMD ["python", "app.py"]