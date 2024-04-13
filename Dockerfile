# Start with a base image containing Python runtime
FROM python:3.11.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y gcc python3-dev musl-dev libmagic1 libffi-dev netcat-traditional \
    build-essential libpq-dev 

# Install Poetry

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip && \
    pip install poetry
# Copy the Python project files into the container at /app
RUN poetry install

COPY . /app/

# RUN chmod +x /app/entrypoint.sh

# COPY . /app/

# ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["poetry", "run", "python", "manage.py", "runserver", "8000"]