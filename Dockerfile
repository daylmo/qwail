# Dockerfile

FROM python:3.13-alpine

ADD . /app
WORKDIR /app
EXPOSE 8000

COPY --from=ghcr.io/astral-sh/uv:0.8.13 /uv /uvx /bin/

RUN uv sync --locked

CMD ["uv", "run", "fastapi", "run", "qwail/main.py", "--host", "0.0.0.0", "--port", "8000"]