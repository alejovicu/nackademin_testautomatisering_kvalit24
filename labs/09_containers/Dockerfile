
FROM mcr.microsoft.com/playwright/python:v1.54.0-noble
RUN pip install pytest-playwright
RUN playwright install
COPY ./test_home.py /home
WORKDIR /home
CMD ["pytest", "-s", "-v"]