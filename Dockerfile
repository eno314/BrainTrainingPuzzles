FROM python:3-slim

RUN pip install --upgrade pip && \
    pip install autopep8 && \
    pip install flake8 && \
    pip install pytest && \
    pip install mypy

WORKDIR /usr/src/app
