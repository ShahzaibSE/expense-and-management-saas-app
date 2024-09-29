
FROM python:latest

LABEL maintainer="shahzaibse"

# Set working directory in the container
WORKDIR /user-service

# Install system dependencies required for potential Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy the Poetry files to the container
COPY pyproject.toml poetry.lock /user-service/

# Install dependencies using Poetry
RUN poetry install --no-root

# Copy the rest of the application code
COPY . /user-service/

# Expose the API Gateway port
EXPOSE 8010

# Run the app. CMD can be overridden when starting the container
CMD [ "poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8010", "--reload"]