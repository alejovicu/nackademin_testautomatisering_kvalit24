FROM mcr.microsoft.com/playwright/python:v1.54.0-noble  

# Set working directory
WORKDIR /workspace

# test script into the container
COPY test_home.py /workspace/

# Install pytest and pytest-playwright
RUN pip install --no-cache-dir pytest pytest-playwright \
    && playwright install

# environment variable to point to your frontend container
ENV APP_FRONT_URL=http://infra-app-frontend-1

CMD ["pytest", "test_home.py"]
