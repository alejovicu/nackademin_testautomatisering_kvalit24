
FROM python:3.9


WORKDIR /test


RUN pip install --no-cache-dir --upgrade pytest-playwright
RUN playwright install --with-deps

COPY ./test_home.py /test/

CMD ["pytest","-v"]