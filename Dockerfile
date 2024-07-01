# Use the official Python image from the Docker Hub
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /home/billing_service_api

# Run apk update and install postgres client
RUN apk update && \
    apk add postgresql-client

# Copy the requirements file to the working directory
COPY ./requirements.txt ./requirements.txt

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY ./app /home/billing_service_api/app
COPY alembic.ini /home/billing_service_api/alembic.ini
COPY ./alembic /home/billing_service_api/alembic
COPY ./bin /home/billing_service_api/bin
COPY ./tests /home/billing_service_api/tests

# Give permissions to entrypoint run as executable
RUN chmod +x /home/billing_service_api/bin/entrypoint

# Run tests
# RUN pytest /home/billing_service_api/tests

# Command to run the FastAPI app
ENTRYPOINT ["/home/billing_service_api/bin/entrypoint"]
