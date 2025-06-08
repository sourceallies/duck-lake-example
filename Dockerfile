FROM ghcr.io/dbt-labs/dbt-core:1.9.latest

ENV PGPASSWORD ''
ENV PGUSER postgres
ENV PGHOST localhost
ENV DATA_S3_PATH ''

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install --requirement requirements.txt

COPY . ./
