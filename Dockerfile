FROM python:3.11-slim

EXPOSE 8000

RUN pip install --no-cache-dir poetry

WORKDIR /cube-api

COPY pyproject.toml ./

RUN poetry install

COPY . ./

CMD [ "poetry", "run", "uvicorn", "--factory", "app:create_app", "--host", "0.0.0.0", "--port", "8000"]