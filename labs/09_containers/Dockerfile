FROM python:3.11-slim

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pytest pytest-playwright
RUN python -m playwright install --with-deps

# Copy test script and any requirements
COPY test_home.py /app/test_home.py
WORKDIR /app

# Set environment variable for frontend URL (kan ändras vid körning)
ENV APP_FRONT_URL=http://172.20.208.1:5173

# Default command to run the test
CMD ["pytest", "test_home.py"]