FROM python:3.9

WORKDIR /app

RUN pip install pytest pytest-playwright \
    && playwright install --with-deps


COPY test_home.py .

CMD ["pytest", "test_home.py"]