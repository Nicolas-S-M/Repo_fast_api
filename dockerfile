FROM python:3.12

RUN apt-get update && apt-get upgrade -y

COPY . /Repo_fast_api

WORKDIR /Repo_fast_api

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

CMD ["uvicorn", "fast_api.app:app", "--host", "0.0.0.0", "--port", "8080"]
