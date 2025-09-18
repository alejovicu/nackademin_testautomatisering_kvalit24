FROM python:3.9

WORKDIR /tests

RUN pip install --no-cache-dir --upgrade pytest-playwright
RUN playwright install --with-deps

#ENV APP_FRONT_URL=http://app-frontend

COPY ./test_home.py /tests/

CMD ["pytest", "-v"]