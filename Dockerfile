FROM python:3.11-slim-bullseye

WORKDIR /opt/

# Install Poetry
RUN pip install poetry
ARG POETRY_VIRTUALENVS_CREATE=false
RUN if [$POETRY_VIRTUALENVS_CREATE == true] ; then poetry config virtualenvs.create true ; else poetry config virtualenvs.create false ; fi

COPY ./pyproject.toml ./poetry.lock* ./

ARG POETRY_INSTALL_DEV=true
RUN if [$POETRY_INSTALL_DEV == true] ; then poetry install --no-root ; else poetry install --no-root --without dev; fi

ARG APP_PATH=/opt/app
COPY app/app $APP_PATH

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
