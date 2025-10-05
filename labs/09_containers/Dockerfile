# Use the official Python image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y \
    libnss3 \
    libatk1.0 \
    libatk-bridge2.0 \
    libcups2 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libxkbcommon0 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    libjpeg62-turbo \
    libxshmfence1 \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Playwright, pytest, and pytest-playwright
RUN pip install --no-cache-dir playwright pytest pytest-playwright

# Install Playwright browsers
RUN playwright install --with-deps

# Copy the test script into the container
COPY test_home.py /app/

# Set the entrypoint to run the test script
ENTRYPOINT ["pytest", "test_home.py"]