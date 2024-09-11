FROM python:3.12-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache gcc musl-dev libffi-dev

COPY . /Repo_fast_api

WORKDIR /Repo_fast_api

RUN pip install poetry alembic

RUN poetry lock && \
    poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

RUN alembic upgrade head

CMD ["poetry", "run", "uvicorn", "fast_api.app:app", "--host", "0.0.0.0", "--port", "8080"]
