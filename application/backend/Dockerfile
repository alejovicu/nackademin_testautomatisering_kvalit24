
FROM python:3.9


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN mkdir /code/routes

COPY ./routes/auth.py /code/routes/
COPY ./routes/products.py /code/routes/
COPY ./routes/users.py /code/routes/

COPY ./auth.py /code/
COPY ./database.py /code/
COPY ./main.py /code/
COPY ./models.py /code/
COPY ./schemas.py /code/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]