FROM python:3.9

WORKDIR /test_app

Run pip install pytest pytest-playwright\
    && playwright install --with-deps

COPY ./test_home.py /test_app/

CMD ["pytest", "test_home.py"]