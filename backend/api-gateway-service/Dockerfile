
FROM python:latest

LABEL maintainer="shahzaibse"

# Set working directory in the container
WORKDIR /api-gateway

# Install system dependencies required for potential Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy the Poetry files to the container
COPY pyproject.toml poetry.lock /app/

# Install dependencies using Poetry
RUN poetry install --no-root

# Copy the rest of the application code
COPY . /api-gateway/

# Expose the API Gateway port
EXPOSE 8000

# Run the app. CMD can be overridden when starting the container
CMD [ "poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]