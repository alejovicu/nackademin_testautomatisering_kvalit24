
FROM python:3.9


WORKDIR /RunTests


RUN pip install --no-cache-dir --upgrade pytest-playwright
RUN playwright install --with-deps

COPY ./test_home.py /RunTests

CMD ["pytest","-v", "-s"]