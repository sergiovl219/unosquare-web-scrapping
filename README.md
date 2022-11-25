# Unosquare Web Scrapping

## Backend Requirements

* [Docker](https://www.docker.com/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

## Backend local development

* Build the image with:

```bash
docker build -t web . --no-cache
```

* Create and Run the Container with:
```bash
docker run --name uno_web_scr -p 80:80 --env-file .env web
```

* Now you can open your browser and interact with these URLs:

Backend, JSON based web API based on OpenAPI: http://localhost/api/

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost/docs

Alternative automatic documentation with ReDoc (from the OpenAPI backend): http://localhost/redoc

* To check the logs, run:

```bash
docker logs uno_web_scr
```

* To open a console inside the container, run:
```bash
docker exec -it uno_web_scr bash
```


## Backend local development, additional details

### General workflow

By default, the dependencies are managed with [Poetry](https://python-poetry.org/), go there and install it.

You can install all the dependencies with:

```console
$ poetry install
```

## Running Tests

```console
$ pytest
```

It will detect the files and tests automatically, execute them, and report the results back to you.
