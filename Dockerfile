FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install fastapi
RUN pip install uvicorn
RUN pip install sqlalchemy

COPY ./app /app