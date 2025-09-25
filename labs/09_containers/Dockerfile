FROM python:3.9

WORKDIR /test_folder

RUN pip install --no-cache-dir pytest pytest-playwright playwright \
    && playwright install --with-deps

COPY ./test_home.py .

CMD ["pytest", "test_home.py"]