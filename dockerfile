#------------------------BUILD STAGE-------------------------#
FROM python:3.13-bookworm AS builder

# Install system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

# Install uv
ADD https://astral.sh/install.sh /tmp/install.sh
RUN chmod +x /tmp/install.sh && /tmp/install.sh && rm /tmp/install.sh

WORKDIR /app

COPY pyproject.toml .

RUN uv sync

#----------------------PRODUCTION STAGE----------------------#
FROM python:3.13-slim-bookworm

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH"

COPY . .

CMD ["uv", "run", "fastapi", "dev", "main.py"]
