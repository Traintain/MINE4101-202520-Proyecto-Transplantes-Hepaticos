FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies (if needed for numpy/pandas/scikit-learn)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Start FastAPI using uvicorn
CMD ["uvicorn", "api_main:app", "--host", "0.0.0.0", "--port", "8000"]

