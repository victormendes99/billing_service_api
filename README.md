# BILLING SERVICE API

A service to upload files and generate Brazilian bank slips (Boletos). This project leverages FastAPI, Async SQLAlchemy, Pydantic, Alembic, and Docker to provide a robust and scalable solution.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Commands](#commands)
  - [Source Environment Variables](#source-environment-variables)
  - [Build Docker Image](#build-docker-image)
  - [Start Service](#start-service)
  - [Run Migrations](#run-migrations)
  - [Stop Service](#stop-service)
- [Running Migrations](#running-migrations)
- [Running the Service](#running-the-service)
- [Testing](#testing)
  - [Run All Tests](#run-all-tests)
  - [Run Integration Tests](#run-integration-tests)
  - [Run Unit Tests](#run-unit-tests)
- [Additional Notes](#additional-notes)

## Prerequisites
- Docker
- Make (optional, but recommended)

If you don't have `make` installed, you can follow [these instructions](https://www.geeksforgeeks.org/how-to-install-make-on-ubuntu/).

## Setup and Installation
Clone the repository and navigate into the project directory:

```sh
git clone https://github.com/yourusername/billing-service-api.git
cd billing-service-api
```

## Commands

### Source Environment Variables
Before running the service, you need to source the environment variables.

```sh
source other-secrets.sh
```

### Build Docker Image
Build the Docker image for the application.

```sh
make build
```

### Start Service
After building the image, you can start the service..
Start the service using:

```sh
make run
```

### Apply Migrations
Apply database migrations using:

```sh
make migrate
```

## Create Migrations
You can manage database migrations with:

```sh
make migration
```

## Testing

### Run All Tests
You can run all tests using:

```sh
make run-test
```

### Run Integration Tests
To run only the integration tests use:

```sh
make run-integration-test
```

### Run Unit Tests
To run only the unit tests use:

```sh
make run-unit-test
```

## Additional Notes
- Ensure Docker is running on your system before executing the commands.
- Customize the environment variables script to include your environment-specific variables.
- You can modify the Makefile to suit your project's specific needs.

By following this guide, you should be able to set up and run the Billing Service API locally with ease. If you encounter any issues, refer to the provided commands and ensure all prerequisites are met.
