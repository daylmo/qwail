# Dockerfile
FROM python:3.13-slim

ENV PYTHONBUFFERED=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD . /app
WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 UV_SYSTEM_PYTHON=1 UV_PYTHON_CACHE_DIR=/root/.cache/uv/python
ENV UV_LINK_MODE=copy
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["fastapi", "run", "qwail/main.py", "--host", "0.0.0.0", "--port", "8000"]
