FROM python:3.9

RUN pip install --no-cache-dir pytest pytest-playwright playwright \
    && playwright install --with-deps

COPY ./test_home.py /test_home.py
CMD ["pytest", "test_home.py"]