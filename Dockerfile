FROM python:3.12-slim-bookworm

# System dependencies for numpy, pandas, scikit-learn, matplotlib
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

# Copy setup files and requirements first
COPY setup.py .
COPY requirements.txt .
COPY src ./src

# Install Python dependencies (editable install will now succeed)
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

CMD ["python3", "app.py"]
