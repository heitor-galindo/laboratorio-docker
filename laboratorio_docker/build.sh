#!/bin/bash

# docker build . -t oficina-python:slim
docker build . -t oficina-python:slim --build-arg python_version=3.8-slim
docker run --rm oficina-python:slim