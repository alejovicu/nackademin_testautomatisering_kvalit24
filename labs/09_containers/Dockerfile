FROM mcr.microsoft.com/playwright/python:v1.42.0-focal

WORKDIR /app

RUN pip install pytest pytest-playwright

RUN playwright install --with-deps

COPY test_home.py .

CMD ["pytest", "test_home.py"]
