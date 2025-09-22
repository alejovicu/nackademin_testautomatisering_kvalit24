FROM python:3.9


WORKDIR /app_tester

RUN pip install pytest pytest-playwright \ 
    && playwright install --with-deps

COPY ./test_home.py /app_tester/

CMD ["pytest", "test_home.py"]
