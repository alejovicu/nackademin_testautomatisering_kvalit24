FROM mcr.microsoft.com/playwright/python:v1.54.0-noble
#FROM python:3.12-bookworm

RUN pip install pytest playwright pytest-playwright && \
    playwright install --with-deps

COPY ./test_home.py ./

CMD ["pytest", "test_home.py"]