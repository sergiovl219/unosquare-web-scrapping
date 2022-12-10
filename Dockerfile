FROM python:3.11-slim-bullseye

WORKDIR /opt/

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_INSTALL_DEV=true \
    APP_PATH=/opt/app \
    PORT=80 \
    HOST=0.0.0.0

# Install Poetry
RUN pip install poetry
RUN poetry config virtualenvs.create $POETRY_VIRTUALENVS_CREATE

COPY ./pyproject.toml ./poetry.lock* ./

RUN if [$POETRY_INSTALL_DEV == true] ; then poetry install --no-root ; else poetry install --no-root --without dev; fi

COPY app/app $APP_PATH

EXPOSE $PORT
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
