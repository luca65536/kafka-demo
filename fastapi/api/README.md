# My Fancy API

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

This is a fancy API built with FastAPI.

## Description

Our Fancy API provides various endpoints to perform actions like retrieving items, filtering data, and more.

## Documentation

Check out the [API Documentation](OUR_FUTURE_URL/docs/api) for detailed information on the available routes, request/response models, and examples.

## Features

- Root endpoint to greet the world
- Endpoint to retrieve items by ID
- Customizable and extensible architecture

## Requirements

- Python 3.7+
- FastAPI
- Pydantic

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/luca65536/kafka-demo
   cd kafka-demo
   ```

2. Setup env
   If you hav setted up our monorepo, you will have venv installed, so just create and source a venv.

   ```bash
   cd myapi
   python3 -m venv env
   source env/bin/activate
   pip install -r ../requirements/development.txt
   ```

3. Start the server:

   ```bash
   uvicorn main:app --reload
   ```

The API will be available at http://localhost:8000.
