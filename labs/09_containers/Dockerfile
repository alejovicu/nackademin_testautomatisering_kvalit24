FROM python:3.9

WORKDIR /tests

RUN pip install pytest pytest-playwright
RUN playwright install --with-deps



COPY ./ test_home.py/ /tests/

CMD ["pytest", "-v"]
