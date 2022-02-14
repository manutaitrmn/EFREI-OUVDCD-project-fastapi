FROM python:3.9

WORKDIR /code

COPY /code /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["hypercorn", "main:app", "--bind", "0.0.0.0:80"]