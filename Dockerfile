FROM python:3.12-slim-bookworm

# Install system dependencies needed for scientific Python packages
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    libatlas-base-dev \
    libopenblas-dev \
    liblapack-dev \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy your project code
COPY . .

# Run the app
CMD ["python3", "app.py"]
