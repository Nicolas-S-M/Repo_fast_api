FROM python:3.12

RUN apt-get update && apt-get upgrade -y

COPY ./fast_api /fast_api

WORKDIR /fast_api

RUN pip install poetry

RUN pwd && ls -la

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

CMD ["uvicorn", "fast_api.app:app", "--host", "0.0.0.0", "--port", "8080"]