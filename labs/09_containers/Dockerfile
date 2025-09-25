FROM python:3.9

WORKDIR /tests

# Playwright package (no cache will be saved in image)
RUN pip install --no-cache-dir playwright

# Playwright browsers with dependencies
RUN playwright install --with-deps

# Pytest and pytest-playwright plugin
RUN pip install --no-cache-dir pytest pytest-playwright

# Copy file from local to WORKDIR
COPY test_home.py .

# Define command when running container
CMD ["pytest", "test_home.py"]



# Run via Docker Compose:    docker run --rm --network infra_default -e APP_FRONT_URL=http://app-frontend test_pw
# Run via local deployment:  docker run --rm -e APP_FRONT_URL=http://(INSERT_LOCAL_IP)):5173 test_pw


