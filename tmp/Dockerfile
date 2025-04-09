FROM ubuntu:24.04

WORKDIR /app

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    libgl1-mesa-dev \
    libx11-6 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libcups2 \
    libnss3 \
    libasound2t64 \
    libatk1.0-0 \
    libgtk-3-0 \
    fonts-freefont-ttf \
    libgstreamer1.0-0 \
    libgtk-4-1 \
    libgraphene-1.0-0 \
    libatomic1 \
    libxslt1.1 \
    libvpx9 \
    libevent-2.1-7t64 \
    libopus0 \
    libgstreamer-plugins-base1.0-0 \
    libgstreamer-plugins-bad1.0-0 \
    libflite1 \
    libwebpdemux2 \
    libavif16 \
    libharfbuzz-icu0 \
    libwebpmux3 \
    libenchant-2-2 \
    libsecret-1-0 \
    libhyphen0 \
    libmanette-0.2-0 \
    libpsl5t64 \
    libnghttp2-14 \
    libx264-164 \
    libwoff1 \
    python3-pip \
    && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

# Copy the Python script
COPY script.py .

RUN playwright install

# Set the entry point for the container
CMD ["python3", "script.py"]

COPY Dockerfile /

